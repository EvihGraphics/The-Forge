 = Get-ChildItem -Path . -File -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 10MB -and $_.FullName -notmatch '\.git\\' }

 = @()
foreach ($file in $files) {
    $relPath = $file.FullName.Substring($PWD.Path.Length + 1).Replace('\', '/')
     += $relPath
}

 | Out-File -Append -Encoding UTF8 .gitignore

foreach ($file in $files) {
    $relPath = $file.FullName.Substring($PWD.Path.Length + 1).Replace('\', '/')
    git rm --cached --ignore-unmatch "$relPath"
}

git reset --soft origin/baseline/theforge-1.58-windows-vs-dx12
git add .
git commit -m "Merge AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced and LocalVisualResults (squashed, >10MB ignored)"
git push origin baseline/theforge-1.58-windows-vs-dx12
