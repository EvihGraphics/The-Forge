# Failure - 36_AlgorithmsAndContainers

Stage: runtime visual capture
Status: MANUAL_INTERACTION_REQUIRED
Category: automation-limited functional test

## Reproduction
Run 36_AlgorithmsAndContainers.exe from the Release x64 output with DX12 arguments through RuntimeLogs/Run-ForgeVisualTest.ps1.

## Summary
The process starts, runs several functional checks successfully, logs UI fallback font warnings, then reports: Bstring tests cannot run without AUTOMATED_TESTING macro. It exits before an accepted visual screenshot can be captured.

## Logs
- VisualResults/36_AlgorithmsAndContainers/Logs/Retry_ResourceAdapt/stdout.txt
- VisualResults/36_AlgorithmsAndContainers/Logs/Retry_ResourceAdapt/stderr.txt
- VisualResults/36_AlgorithmsAndContainers/Logs/Retry_ResourceAdapt/run_metadata.txt

## Blocking AVBOIT
No. This is a low-relevance functional test and does not block transparency development, but it is not a complete green baseline.
