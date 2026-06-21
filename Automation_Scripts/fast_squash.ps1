$staged = git diff --cached --name-only
$largeFiles = @()

foreach ($file in $staged) {
    if (Test-Path $file) {
        $info = Get-Item $file
        if ($info.Length -gt 10485760) {
            $largeFiles += $file
            Write-Host "Found large file: $file"
        }
    }
}

if ($largeFiles.Count -gt 0) {
    "
# Auto-ignored files > 10MB" | Out-File -Append -Encoding UTF8 .gitignore
    foreach ($file in $largeFiles) {
        "$file" | Out-File -Append -Encoding UTF8 .gitignore
        git rm --cached --ignore-unmatch "$file"
    }
}

git add .
git commit -m "Merge Checkpoint and Benchmarks, ignoring files > 10MB"
git push origin baseline/theforge-1.58-windows-vs-dx12
