import os
import subprocess

size_limit = 10 * 1024 * 1024 # 10MB
large_files = []

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        path = os.path.join(root, f)
        if os.path.getsize(path) > size_limit:
            large_files.append(os.path.normpath(path).replace('\\', '/'))

print(f"Found {len(large_files)} large files.")

with open('.gitignore', 'a', encoding='utf-8') as f:
    f.write('\n# Auto-ignored large files (>10MB)\n')
    for lf in large_files:
        f.write(lf + '\n')

for lf in large_files:
    subprocess.run(['git', 'rm', '--cached', '--ignore-unmatch', lf])

subprocess.run(['git', 'reset', '--soft', 'origin/baseline/theforge-1.58-windows-vs-dx12'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Merge Checkpoint, AVBOIT bugfixes, and LocalVisualResults (squashed, >10MB ignored)'])
