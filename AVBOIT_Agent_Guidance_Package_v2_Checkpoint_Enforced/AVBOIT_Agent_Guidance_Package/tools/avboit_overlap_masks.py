#!/usr/bin/env python3
"""Build AVBOIT analytic combined/overlap masks from per-layer coverage PNGs."""

from __future__ import annotations

import argparse
import json
import struct
import sys
import zlib
from pathlib import Path

from avboit_color_parity_metrics import read_png


def pixel_value(pixel: tuple[float, float, float, float]) -> float:
    return max(pixel[0], pixel[1], pixel[2])


def write_gray_png(path: Path, width: int, height: int, values: list[int]) -> None:
    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(tag)
        crc = zlib.crc32(data, crc)
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc & 0xFFFFFFFF)

    raw = bytearray()
    for y in range(height):
        raw.append(0)
        start = y * width
        raw.extend(values[start : start + width])

    png = bytearray()
    png.extend(b"\x89PNG\r\n\x1a\n")
    png.extend(chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0)))
    png.extend(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
    png.extend(chunk(b"IEND", b""))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(bytes(png))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--layers", required=True, nargs="+", type=Path)
    parser.add_argument("--threshold", type=float, default=1.0 / 255.0)
    parser.add_argument("--combined-out", required=True, type=Path)
    parser.add_argument("--overlap-out", required=True, type=Path)
    parser.add_argument("--json-out", required=True, type=Path)
    args = parser.parse_args()

    width = height = None
    layer_masks: list[list[bool]] = []
    layer_counts: list[int] = []
    for layer_path in args.layers:
        lw, lh, pixels = read_png(layer_path)
        if width is None:
            width, height = lw, lh
        elif (lw, lh) != (width, height):
            raise ValueError(f"Layer mask size differs: {layer_path}={lw}x{lh}, expected={width}x{height}")
        mask = [pixel_value(p) > args.threshold for p in pixels]
        layer_masks.append(mask)
        layer_counts.append(sum(1 for v in mask if v))

    assert width is not None and height is not None
    combined: list[int] = []
    overlap: list[int] = []
    combined_count = 0
    overlap_count = 0
    three_way_count = 0
    for i in range(width * height):
        covered_layers = sum(1 for mask in layer_masks if mask[i])
        is_combined = covered_layers > 0
        is_overlap = covered_layers >= 2
        combined_count += int(is_combined)
        overlap_count += int(is_overlap)
        three_way_count += int(covered_layers >= 3)
        combined.append(255 if is_combined else 0)
        overlap.append(255 if is_overlap else 0)

    write_gray_png(args.combined_out, width, height, combined)
    write_gray_png(args.overlap_out, width, height, overlap)

    result = {
        "status": "PASS" if overlap_count > 0 else "FAIL",
        "width": width,
        "height": height,
        "threshold": args.threshold,
        "layerMaskCount": len(layer_masks),
        "perLayerPixelCounts": layer_counts,
        "combinedPixelCount": combined_count,
        "overlapPixelCount": overlap_count,
        "threeWayOverlapPixelCount": three_way_count,
        "combinedMask": str(args.combined_out),
        "overlapMask": str(args.overlap_out),
        "layerMasks": [str(p) for p in args.layers],
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if overlap_count > 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
