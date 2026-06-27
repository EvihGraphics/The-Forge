#!/usr/bin/env python3
"""Validate AVBOIT coverage/resolve-alpha invariant from debug PNG captures."""

from __future__ import annotations

import argparse
import json
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
                raise ValueError(f"{path} uses unsupported PNG compression/filter/interlace settings")
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
                raise ValueError(f"{path} uses unsupported PNG row filter {filter_type}")

        prev = bytes(row)
        rows.append(prev)

    max_value = float((1 << bit_depth) - 1)
    pixels: list[tuple[float, float, float, float]] = []
    for row in rows:
        for x in range(width):
            base = x * bpp
            samples = []
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


def value(pixel: tuple[float, float, float, float]) -> float:
    return max(pixel[0], pixel[1], pixel[2])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coverage", required=True, type=Path, help="Mode 5 debug view 2 PNG")
    parser.add_argument("--opacity", required=True, type=Path, help="Mode 5 debug view 5 PNG")
    parser.add_argument("--threshold", type=float, default=1.0 / 65535.0)
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    args = parser.parse_args()

    cw, ch, coverage_pixels = read_png(args.coverage)
    ow, oh, opacity_pixels = read_png(args.opacity)
    if (cw, ch) != (ow, oh):
        raise ValueError(f"Image sizes differ: coverage={cw}x{ch}, opacity={ow}x{oh}")

    outside_count = 0
    coverage_count = 0
    opacity_count = 0
    outside_sum = 0.0
    outside_max = 0.0

    for coverage_pixel, opacity_pixel in zip(coverage_pixels, opacity_pixels):
        has_coverage = value(coverage_pixel) > args.threshold
        has_opacity = value(opacity_pixel) > args.threshold
        opacity_value = value(opacity_pixel)

        coverage_count += int(has_coverage)
        opacity_count += int(has_opacity)
        if has_opacity and not has_coverage:
            outside_count += 1
            outside_sum += opacity_value
            outside_max = max(outside_max, opacity_value)

    result = {
        "status": "PASS" if outside_count == 0 else "FAIL",
        "width": cw,
        "height": ch,
        "threshold": args.threshold,
        "coveragePixelCount": coverage_count,
        "resolveNonZeroOpacityPixelCount": opacity_count,
        "outsideCoverageNonZeroOpacityPixelCount": outside_count,
        "outsideCoverageMaxOpacity": outside_max,
        "outsideCoverageAverageOpacity": outside_sum / outside_count if outside_count else 0.0,
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for key, val in result.items():
            print(f"{key}: {val}")

    return 0 if outside_count == 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
