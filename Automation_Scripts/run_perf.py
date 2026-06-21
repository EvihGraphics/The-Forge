import subprocess
import os
import re

exe_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe'
log_path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.log'

modes = {
    'WBOIT': 'Test_WeightedBlendedOIT.lua',
    'AOIT': 'Test_AdaptiveOIT.lua',
    'AVBOIT': 'Test_AVBOIT.lua'
}

results = {}

for name, script in modes.items():
    print(f"Running {name}...")
    subprocess.run([exe_path, '--d3d12', '-s', script], cwd=os.path.dirname(exe_path))
    
    # Read the log
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    match = re.search(r'OIT Performance Dump \[Mode \d+\]: ([\d\.]+) ms', log_content)
    if match:
        results[name] = float(match.group(1))
    else:
        results[name] = None

print("\n--- PERFORMANCE RESULTS ---")
for name, time in results.items():
    print(f"{name}: {time} ms")
