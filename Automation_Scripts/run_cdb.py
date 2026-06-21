import subprocess

process = subprocess.Popen(
    ['cdb', '-c', 'g; k; q', 'x64/Release/15_Transparency/15_Transparency.exe', '--d3d12', '--no-auto-exit'],
    cwd='D:/Users/l3d/Documents/AVBOIT/The-Forge/Examples_3/Unit_Tests/PC Visual Studio 2019',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
out, err = process.communicate()

# Extract crash stack
lines = out.split('\n')
start = False
for line in lines:
    if 'Exception' in line or 'Break instruction' in line or 'Access violation' in line:
        start = True
    if start:
        print(line)
