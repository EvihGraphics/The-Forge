import time
import subprocess
from PIL import ImageGrab
import ctypes
import ctypes.wintypes
import os

target_dir = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\LocalVisualResults\HIVE_4090x2\VisualResults\Screenshots'
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

exe_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe'

# WBOIT
print("Testing WBOIT (Mode 1)...")
process = subprocess.Popen([exe_path, '--d3d12', '--no-auto-exit', '-s', 'Test_WeightedBlendedOIT.lua'], cwd=os.path.dirname(exe_path))
time.sleep(8)
hwnd = ctypes.windll.user32.FindWindowW(None, '15_Transparency')
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(1)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
    point = ctypes.wintypes.POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(point))
    screen = ImageGrab.grab(bbox=(point.x, point.y, point.x + rect.right, point.y + rect.bottom))
    screen.save(os.path.join(target_dir, 'UT_15_Transparency_DX12_Mode_1_WBOIT.png'))
process.terminate()
time.sleep(2)

# AVBOIT
print("Testing AVBOIT (Mode 5)...")
process = subprocess.Popen([exe_path, '--d3d12', '--no-auto-exit', '-s', 'Test_AVBOIT.lua'], cwd=os.path.dirname(exe_path))
time.sleep(8)
hwnd = ctypes.windll.user32.FindWindowW(None, '15_Transparency')
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(1)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
    point = ctypes.wintypes.POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(point))
    screen = ImageGrab.grab(bbox=(point.x, point.y, point.x + rect.right, point.y + rect.bottom))
    screen.save(os.path.join(target_dir, 'UT_15_Transparency_DX12_Mode_5_AVBOIT.png'))
process.terminate()

