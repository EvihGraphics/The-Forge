# Soft reset to squash all commits since origin
git reset --soft origin/baseline/theforge-1.58-windows-vs-dx12

# Find files > 10MB in the index
$largeFiles = git ls-files --stage | ForEach-Object {
    $parts = $_ -split '\s+'
    $mode = $parts[0]
    $hash = $parts[1]
    $path = $parts[3]
    
    # We need the size of the blob. We can get it via git cat-file
    $size = git cat-file -s $hash
    if ($size -as [int64] -and [int64]$size -gt 10485760) {
        Write-Output $path
    }
}

# Append to .gitignore and untrack
if ($largeFiles.Count -gt 0) {
    "
# Auto-ignored files > 10MB" | Out-File -Append -Encoding UTF8 .gitignore
    foreach ($file in $largeFiles) {
        "$file" | Out-File -Append -Encoding UTF8 .gitignore
        git rm --cached --ignore-unmatch "$file"
    }
}

# Commit and push
git add .
git commit -m "Merge Checkpoint and Benchmarks, ignoring files > 10MB"
git push origin baseline/theforge-1.58-windows-vs-dx12
