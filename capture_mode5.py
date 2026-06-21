import subprocess, time, ctypes, ctypes.wintypes
import win32gui, win32process, win32ui, win32con
from PIL import Image

# Launch the app
p = subprocess.Popen([
    r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe',
    '--d3d12', '--no-auto-exit', '--transparency-mode=5'
], cwd=r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency')

time.sleep(15)

poll = p.poll()
print(f'Process poll: {poll} (None means running)')

if poll is None:
    pid = p.pid
    print(f'Process PID: {pid}')
    
    def callback(hwnd, results):
        _, wpid = win32process.GetWindowThreadProcessId(hwnd)
        if wpid == pid:
            title = win32gui.GetWindowText(hwnd)
            visible = win32gui.IsWindowVisible(hwnd)
            results.append((hwnd, title, visible))
    
    results = []
    win32gui.EnumWindows(callback, results)
    print(f'Windows for our PID: {results}')
    
    user32 = ctypes.windll.user32
    
    for hwnd, title, vis in results:
        if vis and title == '15_Transparency':
            # Get client rect dimensions
            crect = ctypes.wintypes.RECT()
            user32.GetClientRect(hwnd, ctypes.byref(crect))
            width = crect.right - crect.left
            height = crect.bottom - crect.top
            print(f'Client area: {width}x{height}')
            
            if width > 0 and height > 0:
                # Use PrintWindow with PW_CLIENTONLY (flag=1)
                hwndDC = win32gui.GetWindowDC(hwnd)
                mfcDC = win32ui.CreateDCFromHandle(hwndDC)
                saveDC = mfcDC.CreateCompatibleDC()
                saveBitMap = win32ui.CreateBitmap()
                saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
                saveDC.SelectObject(saveBitMap)
                
                # PW_CLIENTONLY = 1, PW_RENDERFULLCONTENT = 2
                # Try flag=3 (PW_CLIENTONLY | PW_RENDERFULLCONTENT)
                result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
                print(f'PrintWindow result: {result}')
                
                if result:
                    bmpinfo = saveBitMap.GetInfo()
                    bmpstr = saveBitMap.GetBitmapBits(True)
                    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
                    savepath = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\LocalVisualResults\HIVE_4090x2\VisualResults\15_Transparency\Screenshots\UT_15_Transparency_DX12_Mode_5.png'
                    im.save(savepath)
                    print(f'Saved {im.size} to {savepath}')
                else:
                    print('PrintWindow failed, trying flag=2...')
                    result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
                    print(f'PrintWindow(2) result: {result}')
                    if result:
                        bmpinfo = saveBitMap.GetInfo()
                        bmpstr = saveBitMap.GetBitmapBits(True)
                        im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
                        savepath = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\LocalVisualResults\HIVE_4090x2\VisualResults\15_Transparency\Screenshots\UT_15_Transparency_DX12_Mode_5.png'
                        im.save(savepath)
                        print(f'Saved {im.size} to {savepath}')
                
                win32gui.DeleteObject(saveBitMap.GetHandle())
                saveDC.DeleteDC()
                mfcDC.DeleteDC()
                win32gui.ReleaseDC(hwnd, hwndDC)
            break

p.terminate()
print('Done')
