import time
import subprocess
from PIL import ImageGrab
import ctypes
import os

exe_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe'
process = subprocess.Popen([exe_path, '--d3d12', '--no-auto-exit'], cwd=os.path.dirname(exe_path))

time.sleep(10)

hwnd = ctypes.windll.user32.FindWindowW(None, '15_Transparency')
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(2)
    
    # We don't have lua to switch dynamically, so let's use UI clicks!
    # X = 345, Y = 468
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    # Assuming DPI 1.25, let's just click the dropdown
    x = rect.left + 345
    y = rect.top + 468
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.5)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left up
    time.sleep(0.5)
    
    # Press HOME
    ctypes.windll.user32.keybd_event(0x24, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(0x24, 0, 2, 0)
    time.sleep(0.5)
    
    # Press DOWN 6 times
    for _ in range(6):
        ctypes.windll.user32.keybd_event(0x28, 0, 0, 0)
        time.sleep(0.1)
        ctypes.windll.user32.keybd_event(0x28, 0, 2, 0)
        time.sleep(0.1)
        
    # Press ENTER to select
    ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
    time.sleep(5)
    
    # Capture screen
    screen = ImageGrab.grab()
    screen.save(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\Dynamic_Test.png')

process.terminate()
