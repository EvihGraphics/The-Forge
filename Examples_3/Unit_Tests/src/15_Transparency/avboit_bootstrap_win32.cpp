// avboit_bootstrap_win32.cpp
// Provides the Windows-only stub implementation of avboitBootstrapStage.
// This function is called from 15_Transparency.cpp to signal capture pipeline
// milestones (stage names appear in stdout so the Python capture script can
// synchronise). The implementation here simply prints to stdout and flushes.

#include <cstdio>

void avboitBootstrapStage(const char* stage)
{
    if (stage)
    {
        printf("AVBOIT_STAGE:%s\n", stage);
        fflush(stdout);
    }
}
