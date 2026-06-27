#!/usr/bin/env python3
"""Compute AVBOIT color parity metrics from PNG captures using only stdlib."""

from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import zlib
from pathlib import Path


PNG_SIG = b"\x89PNG\r\n\x1a\n"


def paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png(path: Path) -> tuple[int, int, list[tuple[float, float, float, float]]]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIG):
        raise ValueError(f"{path} is not a PNG file")

    pos = len(PNG_SIG)
    width = height = bit_depth = color_type = None
    idat = bytearray()

    while pos < len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        pos += 4
        chunk_type = data[pos : pos + 4]
        pos += 4
        chunk = data[pos : pos + length]
        pos += length + 4
        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack(">IIBBBBB", chunk)
            if compression != 0 or filter_method != 0 or interlace != 0:
                raise ValueError(f"{path} uses unsupported PNG settings")
        elif chunk_type == b"IDAT":
            idat.extend(chunk)
        elif chunk_type == b"IEND":
            break

    if width is None or height is None or bit_depth is None or color_type is None:
        raise ValueError(f"{path} is missing IHDR")
    if bit_depth not in (8, 16):
        raise ValueError(f"{path} uses unsupported bit depth {bit_depth}")

    channels_by_type = {0: 1, 2: 3, 4: 2, 6: 4}
    if color_type not in channels_by_type:
        raise ValueError(f"{path} uses unsupported PNG color type {color_type}")

    channels = channels_by_type[color_type]
    bytes_per_sample = bit_depth // 8
    bpp = channels * bytes_per_sample
    stride = width * bpp
    raw = zlib.decompress(bytes(idat))
    rows: list[bytes] = []
    prev = bytes(stride)
    cursor = 0

    for _ in range(height):
        filter_type = raw[cursor]
        cursor += 1
        row = bytearray(raw[cursor : cursor + stride])
        cursor += stride
        for i in range(stride):
            left = row[i - bpp] if i >= bpp else 0
            up = prev[i]
            upper_left = prev[i - bpp] if i >= bpp else 0
            if filter_type == 1:
                row[i] = (row[i] + left) & 0xFF
            elif filter_type == 2:
                row[i] = (row[i] + up) & 0xFF
            elif filter_type == 3:
                row[i] = (row[i] + ((left + up) >> 1)) & 0xFF
            elif filter_type == 4:
                row[i] = (row[i] + paeth(left, up, upper_left)) & 0xFF
            elif filter_type != 0:
                raise ValueError(f"{path} uses unsupported PNG filter {filter_type}")
        prev = bytes(row)
        rows.append(prev)

    max_value = float((1 << bit_depth) - 1)
    pixels: list[tuple[float, float, float, float]] = []
    for row in rows:
        for x in range(width):
            base = x * bpp
            samples: list[float] = []
            for c in range(channels):
                off = base + c * bytes_per_sample
                if bit_depth == 8:
                    samples.append(row[off] / max_value)
                else:
                    samples.append(struct.unpack(">H", row[off : off + 2])[0] / max_value)
            if color_type == 0:
                r = g = b = samples[0]
                a = 1.0
            elif color_type == 2:
                r, g, b = samples
                a = 1.0
            elif color_type == 4:
                r = g = b = samples[0]
                a = samples[1]
            else:
                r, g, b, a = samples
            pixels.append((r, g, b, a))
    return width, height, pixels


def srgb_to_linear(v: float) -> float:
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def luma(p: tuple[float, float, float, float]) -> float:
    return 0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]


def ssim(values_a: list[float], values_b: list[float]) -> float:
    n = len(values_a)
    if n == 0:
        return 1.0
    mean_a = sum(values_a) / n
    mean_b = sum(values_b) / n
    var_a = sum((v - mean_a) ** 2 for v in values_a) / n
    var_b = sum((v - mean_b) ** 2 for v in values_b) / n
    cov = sum((a - mean_a) * (b - mean_b) for a, b in zip(values_a, values_b)) / n
    c1 = 0.01 ** 2
    c2 = 0.03 ** 2
    return ((2 * mean_a * mean_b + c1) * (2 * cov + c2)) / ((mean_a * mean_a + mean_b * mean_b + c1) * (var_a + var_b + c2))


def compute_metrics(ref: list[tuple[float, float, float, float]], cand: list[tuple[float, float, float, float]]) -> dict[str, float | int]:
    count = len(ref)
    abs_rgb = 0.0
    abs_linear_rgb = 0.0
    abs_luma = 0.0
    signed_luma = 0.0
    max_rgb = 0.0
    mse = 0.0
    dark = 0
    bright = 0
    ref_luma: list[float] = []
    cand_luma: list[float] = []

    for a, b in zip(ref, cand):
        la = luma(a)
        lb = luma(b)
        ref_luma.append(la)
        cand_luma.append(lb)
        abs_luma += abs(lb - la)
        signed_luma += lb - la
        dark += int(lb < la - (2.0 / 255.0))
        bright += int(lb > la + (2.0 / 255.0))
        for c in range(3):
            diff = b[c] - a[c]
            abs_rgb += abs(diff)
            max_rgb = max(max_rgb, abs(diff))
            mse += diff * diff
            abs_linear_rgb += abs(srgb_to_linear(b[c]) - srgb_to_linear(a[c]))

    denom_rgb = max(count * 3, 1)
    mse /= denom_rgb
    psnr = 99.0 if mse <= 1e-16 else 10.0 * math.log10(1.0 / mse)
    return {
        "pixelCount": count,
        "rgbMae": abs_rgb / denom_rgb,
        "linearRgbMae": abs_linear_rgb / denom_rgb,
        "lumaMae": abs_luma / max(count, 1),
        "signedLumaDiff": signed_luma / max(count, 1),
        "rgbMaxAbsDiff": max_rgb,
        "psnr": psnr,
        "ssimLuma": ssim(ref_luma, cand_luma),
        "darkPixelCount": dark,
        "brightPixelCount": bright,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    rw, rh, ref = read_png(args.reference)
    cw, ch, cand = read_png(args.candidate)
    if (rw, rh) != (cw, ch):
        raise ValueError(f"Image sizes differ: reference={rw}x{rh}, candidate={cw}x{ch}")

    result = {
        "reference": str(args.reference),
        "candidate": str(args.candidate),
        "width": rw,
        "height": rh,
        **compute_metrics(ref, cand),
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
