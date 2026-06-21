import time
import subprocess
from PIL import ImageGrab
import ctypes
import os

# Start the application
exe_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe'
process = subprocess.Popen([exe_path, '--d3d12', '--no-auto-exit'], cwd=os.path.dirname(exe_path))

time.sleep(10) # Wait for it to load

# Use ctypes to find window and bring to front
hwnd = ctypes.windll.user32.FindWindowW(None, '15_Transparency')
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(2)
    
    # Simulate pressing DOWN arrow 6 times to select Mode 6!
    # Or just capture the whole screen
    # Wait, if we don't press DOWN, it defaults to Mode 0!
    # Let's simulate clicking the dropdown.
    # Actually, let's just grab the screen first to see where the UI is!
    
    screen = ImageGrab.grab()
    screen.save(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\FullScreenCapture.png')

process.terminate()
