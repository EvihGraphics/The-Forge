import argparse

import numpy as np
from PIL import Image


def describe(label: str, path: str) -> None:
    image = Image.open(path).convert("RGB")
    arr = np.array(image)
    height, width = arr.shape[:2]
    center = arr[height // 4 : 3 * height // 4, width // 4 : 3 * width // 4]
    corner = arr[:100, :100]
    print(f"{label} path: {path}")
    print(f"{label} Max RGB: {arr.max(axis=(0, 1))}")
    print(f"{label} Mean RGB: {arr.mean(axis=(0, 1))}")
    print(f"{label} Center Mean: {center.mean(axis=(0, 1))}")
    print(f"{label} Center Max:  {center.max(axis=(0, 1))}")
    print(f"{label} Corner Mean: {corner.mean(axis=(0, 1))}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Print image statistics for AVBOIT visual captures.")
    parser.add_argument(
        "--avboit",
        default="LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5_AVBOIT.png",
    )
    parser.add_argument(
        "--wboit",
        default="LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_1_WBOIT.png",
    )
    args = parser.parse_args()

    describe("AVBOIT", args.avboit)
    print()
    describe("WBOIT", args.wboit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
