import time
import subprocess
from PIL import ImageGrab
import ctypes
import os

exe_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe'
process = subprocess.Popen([exe_path, '--d3d12', '--no-auto-exit', '-s', 'Test_AVBOIT.lua'], cwd=os.path.dirname(exe_path))

time.sleep(10)

hwnd = ctypes.windll.user32.FindWindowW(None, '15_Transparency')
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(2)
    screen = ImageGrab.grab()
    screen.save(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\AVBOIT_Fixed_Screen.png')

process.terminate()
