import argparse
import ctypes
import ctypes.wintypes
import os
import subprocess
import time

import numpy as np
from PIL import ImageGrab


def main() -> int:
    parser = argparse.ArgumentParser(description="Launch 15_Transparency and capture the default DX12 view.")
    parser.add_argument(
        "--exe",
        default=os.path.join(
            os.getcwd(),
            "Examples_3",
            "Unit_Tests",
            "PC Visual Studio 2019",
            "x64",
            "Release",
            "15_Transparency",
            "15_Transparency.exe",
        ),
        help="Path to 15_Transparency.exe.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join("LocalVisualResults", "HIVE_4090x2", "VisualResults", "Diagnostics"),
        help="Directory for the captured PNG.",
    )
    parser.add_argument("--output-name", default="AVBOIT_Default_Mode_Test.png")
    parser.add_argument("--wait-seconds", type=float, default=10.0)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    process = subprocess.Popen([args.exe, "--d3d12"], cwd=os.path.dirname(args.exe))
    try:
        time.sleep(args.wait_seconds)
        hwnd = ctypes.windll.user32.FindWindowW(None, "15_Transparency")
        print(f"Window handle: {hwnd}")
        if not hwnd:
            print("Window not found.")
            return 2

        ctypes.windll.user32.ShowWindow(hwnd, 9)
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        time.sleep(2)

        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
        point = ctypes.wintypes.POINT(0, 0)
        ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(point))
        width, height = rect.right, rect.bottom
        print(f"Client rect: {width}x{height} at ({point.x},{point.y})")

        screen = ImageGrab.grab(bbox=(point.x, point.y, point.x + width, point.y + height))
        output_path = os.path.join(args.output_dir, args.output_name)
        screen.save(output_path)

        arr = np.array(screen.convert("RGB"))
        print(f"Saved: {output_path}")
        print(f"Mean RGB: {arr.mean(axis=(0, 1))}")
        print(f"Max RGB: {arr.max(axis=(0, 1))}")
        center = arr[height // 4 : 3 * height // 4, width // 4 : 3 * width // 4]
        print(f"Center Mean RGB: {center.mean(axis=(0, 1))}")
        print(f"Center Max RGB: {center.max(axis=(0, 1))}")
        return 0
    finally:
        process.terminate()


if __name__ == "__main__":
    raise SystemExit(main())
