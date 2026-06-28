/*
 * Copyright (c) 2017-2024 The Forge Interactive Inc.
 *
 * This file is part of The-Forge
 * (see https://github.com/ConfettiFX/The-Forge).
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

#include "../../Application/Config.h"

#ifdef _WINDOWS

#include <ctime>
#include <exception>
#include <signal.h>
#include <ntverp.h>

#include "../CPUConfig.h"

#if !defined(XBOX)
#include <shlwapi.h>
#pragma comment(lib, "shlwapi.lib")
#endif

#include "../../Utilities/ThirdParty/OpenSource/Nothings/stb_ds.h"
#include "../../Utilities/ThirdParty/OpenSource/bstrlib/bstrlib.h"
#include "../../Utilities/ThirdParty/OpenSource/rmem/inc/rmem.h"

#include "../../Application/Interfaces/IApp.h"
#include "../../Application/Interfaces/IFont.h"
#include "../../Application/Interfaces/IProfiler.h"
#include "../../Application/Interfaces/IUI.h"
#include "../../Game/Interfaces/IScripting.h"
#include "../../Graphics/Interfaces/IGraphics.h"
#include "../../OS/Interfaces/IOperatingSystem.h"
#include "../../Utilities/Interfaces/IFileSystem.h"
#include "../../Utilities/Interfaces/ILog.h"
#include "../../Utilities/Interfaces/IThread.h"
#include "../../Utilities/Interfaces/ITime.h"

#if defined(ENABLE_FORGE_REMOTE_UI)
#include "../../Tools/Network/Network.h"
#endif
#if defined(ENABLE_FORGE_RELOAD_SHADER)
#include "../../Tools/ReloadServer/ReloadClient.h"
#endif
#include "../../Utilities/Math/MathTypes.h"

#include "../../Utilities/Interfaces/IMemory.h"

#ifdef ENABLE_FORGE_STACKTRACE_DUMP
#include "WindowsStackTraceDump.h"
#endif

#define elementsOf(a) (sizeof(a) / sizeof((a)[0]))

// App Data
static IApp*       pApp = nullptr;
static WindowDesc* gWindowDesc = nullptr;
static bool        gShowPlatformUI = true;
static ResetDesc   gResetDescriptor = { RESET_TYPE_NONE };
static ReloadDesc  gReloadDescriptor = { RELOAD_TYPE_ALL };
/// CPU
static CpuInfo     gCpu;
static OSInfo      gOsInfo = {};

static bool   gAVBOITBootstrapLogEnabled = false;
static HANDLE gAVBOITBootstrapLogFile = INVALID_HANDLE_VALUE;
static char   gAVBOITBootstrapLastStage[128] = "not-started";

static bool AVBOITBootstrapArgEquals(const char* arg, const char* name)
{
    return arg && name && strcmp(arg, name) == 0;
}

static bool AVBOITBootstrapArgValue(const char* arg, const char* prefix, char* outValue, size_t outValueSize)
{
    if (!arg || !prefix || !outValue || outValueSize == 0)
        return false;

    const size_t prefixLength = strlen(prefix);
    if (strncmp(arg, prefix, prefixLength) != 0)
        return false;

    strncpy(outValue, arg + prefixLength, outValueSize - 1);
    outValue[outValueSize - 1] = 0;
    return true;
}

static void AVBOITBootstrapMakeDirectory(const char* path)
{
    if (!path || !path[0])
        return;

    char partial[MAX_PATH] = {};
    strncpy(partial, path, sizeof(partial) - 1);
    partial[sizeof(partial) - 1] = 0;

    for (char* cursor = partial; *cursor; ++cursor)
    {
        if (*cursor != '\\' && *cursor != '/')
            continue;
        if (cursor == partial || (cursor > partial && cursor[-1] == ':'))
            continue;

        const char separator = *cursor;
        *cursor = 0;
        CreateDirectoryA(partial, NULL);
        *cursor = separator;
    }

    CreateDirectoryA(partial, NULL);
}

static void AVBOITBootstrapWriteRaw(const char* text)
{
    if (!gAVBOITBootstrapLogEnabled || gAVBOITBootstrapLogFile == INVALID_HANDLE_VALUE || !text)
        return;

    DWORD written = 0;
    WriteFile(gAVBOITBootstrapLogFile, text, (DWORD)strlen(text), &written, NULL);
    FlushFileBuffers(gAVBOITBootstrapLogFile);
}

static void AVBOITBootstrapWrite(const char* stage)
{
    if (!stage || !stage[0])
        return;

    strncpy(gAVBOITBootstrapLastStage, stage, sizeof(gAVBOITBootstrapLastStage) - 1);
    gAVBOITBootstrapLastStage[sizeof(gAVBOITBootstrapLastStage) - 1] = 0;

    SYSTEMTIME time = {};
    GetLocalTime(&time);
    char line[512] = {};
    snprintf(line, sizeof(line), "%04u-%02u-%02uT%02u:%02u:%02u.%03u %s\n", (uint32_t)time.wYear, (uint32_t)time.wMonth,
             (uint32_t)time.wDay, (uint32_t)time.wHour, (uint32_t)time.wMinute, (uint32_t)time.wSecond,
             (uint32_t)time.wMilliseconds, stage);
    AVBOITBootstrapWriteRaw(line);
}

void avboitBootstrapStage(const char* stage) { AVBOITBootstrapWrite(stage); }

static LONG WINAPI AVBOITBootstrapUnhandledException(EXCEPTION_POINTERS* exceptionInfo)
{
    char line[512] = {};
    const DWORD code = exceptionInfo && exceptionInfo->ExceptionRecord ? exceptionInfo->ExceptionRecord->ExceptionCode : 0;
    const void* address = exceptionInfo && exceptionInfo->ExceptionRecord ? exceptionInfo->ExceptionRecord->ExceptionAddress : NULL;
    snprintf(line, sizeof(line), "UNHANDLED_EXCEPTION code=0x%08x address=%p lastStage=%s\n", code, address, gAVBOITBootstrapLastStage);
    AVBOITBootstrapWriteRaw(line);
    return EXCEPTION_EXECUTE_HANDLER;
}

static void AVBOITBootstrapTerminate()
{
    char line[256] = {};
    snprintf(line, sizeof(line), "TERMINATE lastStage=%s\n", gAVBOITBootstrapLastStage);
    AVBOITBootstrapWriteRaw(line);
    abort();
}

static void AVBOITBootstrapSignalHandler(int signalNumber)
{
    char line[256] = {};
    snprintf(line, sizeof(line), "SIGNAL signal=%d lastStage=%s\n", signalNumber, gAVBOITBootstrapLastStage);
    AVBOITBootstrapWriteRaw(line);
    signal(signalNumber, SIG_DFL);
    raise(signalNumber);
}

static void AVBOITBootstrapConfigure(int argc, char** argv, const char* appName)
{
    bool autoCapture = false;
    char explicitLogDir[MAX_PATH] = {};
    char outputDir[MAX_PATH] = {};

    for (int i = 0; i < argc; ++i)
    {
        autoCapture = autoCapture || AVBOITBootstrapArgEquals(argv[i], "--avboit-auto-capture");
        AVBOITBootstrapArgValue(argv[i], "--avboit-bootstrap-log-dir=", explicitLogDir, sizeof(explicitLogDir));
        AVBOITBootstrapArgValue(argv[i], "--avboit-output-dir=", outputDir, sizeof(outputDir));
    }

    if (!explicitLogDir[0] && autoCapture && outputDir[0])
        snprintf(explicitLogDir, sizeof(explicitLogDir), "%s\\bootstrap", outputDir);

    if (!explicitLogDir[0])
        return;

    AVBOITBootstrapMakeDirectory(explicitLogDir);

    SYSTEMTIME time = {};
    GetLocalTime(&time);
    char logPath[MAX_PATH] = {};
    snprintf(logPath, sizeof(logPath), "%s\\avboit_bootstrap_%04u%02u%02uT%02u%02u%02u_%lu.log", explicitLogDir,
             (uint32_t)time.wYear, (uint32_t)time.wMonth, (uint32_t)time.wDay, (uint32_t)time.wHour, (uint32_t)time.wMinute,
             (uint32_t)time.wSecond, GetCurrentProcessId());

    gAVBOITBootstrapLogFile = CreateFileA(logPath, GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    gAVBOITBootstrapLogEnabled = gAVBOITBootstrapLogFile != INVALID_HANDLE_VALUE;
    if (!gAVBOITBootstrapLogEnabled)
        return;

    SetUnhandledExceptionFilter(AVBOITBootstrapUnhandledException);
    std::set_terminate(AVBOITBootstrapTerminate);
    signal(SIGABRT, AVBOITBootstrapSignalHandler);
    signal(SIGFPE, AVBOITBootstrapSignalHandler);
    signal(SIGILL, AVBOITBootstrapSignalHandler);
    signal(SIGSEGV, AVBOITBootstrapSignalHandler);
    signal(SIGTERM, AVBOITBootstrapSignalHandler);

    AVBOITBootstrapWrite("BOOTSTRAP_START");

    char cwd[MAX_PATH] = {};
    GetCurrentDirectoryA(sizeof(cwd), cwd);
    char line[2048] = {};
    snprintf(line, sizeof(line), "APP_NAME %s\nPROCESS_ID %lu\nWORKING_DIRECTORY %s\nCOMMAND_LINE %s\nOUTPUT_DIRECTORY %s\nLOG_DIRECTORY %s\n",
             appName ? appName : "unknown", GetCurrentProcessId(), cwd, GetCommandLineA(), outputDir[0] ? outputDir : "(default)",
             explicitLogDir);
    AVBOITBootstrapWriteRaw(line);
}

static void AVBOITBootstrapClose()
{
    AVBOITBootstrapWrite("APP_EXITED");
    if (gAVBOITBootstrapLogFile != INVALID_HANDLE_VALUE)
    {
        CloseHandle(gAVBOITBootstrapLogFile);
        gAVBOITBootstrapLogFile = INVALID_HANDLE_VALUE;
    }
    gAVBOITBootstrapLogEnabled = false;
}

// UI
static UIComponent* pAPISwitchingComponent = NULL;
static UIComponent* pToggleVSyncComponent = NULL;
#if defined(ENABLE_FORGE_RELOAD_SHADER)
static UIComponent* pReloadShaderComponent = NULL;
#endif
static UIWidget* pSwitchComponentLabelWidget = NULL;
static UIWidget* pSelectApUIWidget = NULL;
static UIWidget* pSelectGraphicCardWidget = NULL;
static uint32_t  gSelectedApiIndex = 0;

// PickRenderingAPI.cpp
extern PlatformParameters gPlatformParameters;
extern bool               gD3D11Unsupported;

// WindowsWindow.cpp
extern IApp*        pWindowAppRef;
extern WindowDesc*  gWindow;
extern bool         gCursorVisible;
extern bool         gCursorInsideRectangle;
extern MonitorDesc* gMonitors;
extern uint32_t     gMonitorCount;

// WindowsLog.c
extern "C" HWND* gLogWindowHandle;

//------------------------------------------------------------------------
// STATIC HELPER FUNCTIONS
//------------------------------------------------------------------------

static inline float CounterToSecondsElapsed(int64_t start, int64_t end) { return (float)(end - start) / (float)1e6; }

static const char* RendererApiToString(RendererApi api)
{
    switch (api)
    {
#if defined(GLES)
    case RENDERER_API_GLES:
        return "GLES";
#endif
#if defined(DIRECT3D12)
    case RENDERER_API_D3D12:
        return "D3D12";
#endif
#if defined(VULKAN)
    case RENDERER_API_VULKAN:
        return "Vulkan";
#endif
#if defined(DIRECT3D11)
    case RENDERER_API_D3D11:
        return "D3D11";
#endif
#if defined(METAL)
    case RENDERER_API_METAL:
        return "Metal";
#endif
#if defined(ORBIS)
    case RENDERER_API_ORBIS:
        return "Orbis";
#endif
#if defined(PROSPERO)
    case RENDERER_API_PROSPERO:
        return "Prospero";
#endif
    default:
        return "Unknown";
    }
}

static bool     gCommandLineRendererApiRequested = false;
static RendererApi gCommandLineRendererApi = RENDERER_API_COUNT;

static bool SelectRendererApiFromCommandLine(RendererApi api, const char* pName)
{
    if (gCommandLineRendererApiRequested)
    {
        LOGF(eERROR, "Multiple command line parameters are requesting the rendering API, only one is allowed.");
        return false;
    }

    gPlatformParameters.mSelectedRendererApi = api;
    gCommandLineRendererApi = api;
    gCommandLineRendererApiRequested = true;
    LOGF(LogLevel::eINFO, "Requested Renderer API: %s", pName);
    return true;
}

static bool ParseRendererApiCommandLine(int argc, char** argv)
{
    gCommandLineRendererApiRequested = false;
    gCommandLineRendererApi = RENDERER_API_COUNT;

    for (int i = 0; i < argc; ++i)
    {
        if (strcmp(argv[i], "--d3d11") == 0)
        {
#if defined(DIRECT3D11)
            if (!SelectRendererApiFromCommandLine(RENDERER_API_D3D11, "D3D11"))
                return false;
#else
            LOGF(eERROR, "Command line requested D3D11, but this build does not include Direct3D 11.");
            return false;
#endif
        }
        else if (strcmp(argv[i], "--d3d12") == 0)
        {
#if defined(DIRECT3D12)
            if (!SelectRendererApiFromCommandLine(RENDERER_API_D3D12, "D3D12"))
                return false;
#else
            LOGF(eERROR, "Command line requested D3D12, but this build does not include Direct3D 12.");
            return false;
#endif
        }
        else if (strcmp(argv[i], "--vulkan") == 0)
        {
#if defined(VULKAN)
            if (!SelectRendererApiFromCommandLine(RENDERER_API_VULKAN, "Vulkan"))
                return false;
#else
            LOGF(eERROR, "Command line requested Vulkan, but this build does not include Vulkan.");
            return false;
#endif
        }
    }

    if (!gCommandLineRendererApiRequested)
        LOGF(LogLevel::eINFO, "Requested Renderer API: default");

    LOGF(LogLevel::eINFO, "Selected Renderer API before initialization: %s", RendererApiToString(gPlatformParameters.mSelectedRendererApi));
    return true;
}

ThermalStatus getThermalStatus() { return THERMAL_STATUS_NOT_SUPPORTED; }

//------------------------------------------------------------------------
// OPERATING SYSTEM INTERFACE FUNCTIONS
//------------------------------------------------------------------------

void requestShutdown() { PostQuitMessage(0); }

void requestReset(const ResetDesc* pResetDesc) { gResetDescriptor = *pResetDesc; }

void requestReload(const ReloadDesc* pReloadDesc) { gReloadDescriptor = *pReloadDesc; }

void errorMessagePopup(const char* title, const char* msg, WindowHandle* handle, errorMessagePopupCallbackFn callback)
{
    UNREF_PARAM(handle);
#if defined(AUTOMATED_TESTING)
    LOGF(eERROR, title);
    LOGF(eERROR, msg);
#else
    MessageBoxA((HWND)handle->window, msg, title, MB_OK);
#endif
    if (callback)
    {
        callback();
    }
}

CustomMessageProcessor sCustomProc = nullptr;
void                   setCustomMessageProcessor(CustomMessageProcessor proc) { sCustomProc = proc; }

CpuInfo* getCpuInfo() { return &gCpu; }

OSInfo* getOsInfo() { return &gOsInfo; }

void getOsVersion(ULONG& majorVersion, ULONG& minorVersion, ULONG& buildNumber)
{
    void(WINAPI * pfnRtlGetNtVersionNumbers)(__out_opt ULONG * pNtMajorVersion, __out_opt ULONG * pNtMinorVersion,
                                             __out_opt ULONG * pNtBuildNumber);

    (FARPROC&)pfnRtlGetNtVersionNumbers = GetProcAddress(GetModuleHandle(L"ntdll.dll"), "RtlGetNtVersionNumbers");

    if (pfnRtlGetNtVersionNumbers)
    {
        pfnRtlGetNtVersionNumbers(&majorVersion, &minorVersion, &buildNumber);
        buildNumber = buildNumber & ~0xF0000000;
    }
}
//------------------------------------------------------------------------
// PLATFORM LAYER CORE SUBSYSTEMS
//------------------------------------------------------------------------

bool initBaseSubsystems()
{
    // Not exposed in the interface files / app layer
    extern bool platformInitFontSystem();
    extern bool platformInitUserInterface();
    extern void platformInitLuaScriptingSystem();
    extern void platformInitWindowSystem(WindowDesc*);

    platformInitWindowSystem(gWindowDesc);
    pApp->pWindow = gWindowDesc;

#ifdef ENABLE_FORGE_FONTS
    if (!platformInitFontSystem())
        return false;
#endif

#ifdef ENABLE_FORGE_UI
    if (!platformInitUserInterface())
        return false;
#endif

#ifdef ENABLE_FORGE_SCRIPTING
    platformInitLuaScriptingSystem();

#if defined(ENABLE_FORGE_SCRIPTING) && defined(AUTOMATED_TESTING)
    // Tests below are executed first, before any tests registered in IApp::Init
    const char*    sFirstTestScripts[] = { "Test_Default.lua" };
    const uint32_t numScripts = sizeof(sFirstTestScripts) / sizeof(sFirstTestScripts[0]);
    LuaScriptDesc  scriptDescs[numScripts] = {};
    for (uint32_t i = 0; i < numScripts; ++i)
    {
        scriptDescs[i].pScriptFileName = sFirstTestScripts[i];
    }
    luaDefineScripts(scriptDescs, numScripts);
#endif
#endif

#if defined(ENABLE_FORGE_REMOTE_UI)
    initNetwork();
#endif

    return true;
}

void updateBaseSubsystems(float deltaTime, bool appDrawn)
{
    // Not exposed in the interface files / app layer
    extern void platformUpdateLuaScriptingSystem(bool appDrawn);
    extern void platformUpdateUserInterface(float deltaTime);
    extern void platformUpdateWindowSystem();

    platformUpdateWindowSystem();

#ifdef ENABLE_FORGE_SCRIPTING
    platformUpdateLuaScriptingSystem(appDrawn);
#endif

#ifdef ENABLE_FORGE_UI
    platformUpdateUserInterface(deltaTime);
#endif
}

void exitBaseSubsystems()
{
    // Not exposed in the interface files / app layer
    extern void platformExitFontSystem();
    extern void platformExitUserInterface();
    extern void platformExitLuaScriptingSystem();
    extern void platformExitWindowSystem();

    platformExitWindowSystem();

#ifdef ENABLE_FORGE_UI
    platformExitUserInterface();
#endif

#ifdef ENABLE_FORGE_FONTS
    platformExitFontSystem();
#endif

#ifdef ENABLE_FORGE_SCRIPTING
    platformExitLuaScriptingSystem();
#endif

#if defined(ENABLE_FORGE_REMOTE_UI)
    exitNetwork();
#endif
}

//------------------------------------------------------------------------
// PLATFORM LAYER USER INTERFACE
//------------------------------------------------------------------------

// Must be called after Graphics::initRenderer()
void setupPlatformUI(const IApp::Settings* pSettings)
{
    gSelectedApiIndex = gPlatformParameters.mSelectedRendererApi;

#ifdef ENABLE_FORGE_UI

    // WINDOW AND RESOLUTION CONTROL
    extern void platformSetupWindowSystemUI(IApp*);
    platformSetupWindowSystemUI(pApp);

    // VSYNC CONTROL
    UIComponentDesc uiDesc = {};
    uiDesc.mStartPosition = vec2(pSettings->mWidth * 0.7f, pSettings->mHeight * 0.8f);
    uiCreateComponent("VSync Control", &uiDesc, &pToggleVSyncComponent);

    CheckboxWidget checkbox;
    checkbox.pData = &pApp->mSettings.mVSyncEnabled;
    UIWidget* pCheckbox = uiCreateComponentWidget(pToggleVSyncComponent, "Toggle VSync\t\t\t\t\t", &checkbox, WIDGET_TYPE_CHECKBOX);
    REGISTER_LUA_WIDGET(pCheckbox);

    // MICROPROFILER UI
    toggleProfilerMenuUI(true);

#if defined(ENABLE_FORGE_RELOAD_SHADER)
    // RELOAD CONTROL
    uiDesc = {};
    uiDesc.mStartPosition = vec2(pSettings->mWidth * 0.7f, pSettings->mHeight * 0.9f);
    uiCreateComponent("Reload Control", &uiDesc, &pReloadShaderComponent);

    platformReloadClientAddReloadShadersButton(pReloadShaderComponent);
#endif

    // API SWITCHING
    uiDesc = {};
    uiDesc.mStartPosition = vec2(pSettings->mWidth * 0.6f, pSettings->mHeight * 0.01f);
    uiCreateComponent("API Switching", &uiDesc, &pAPISwitchingComponent);

    static const char* pApiNames[] = {
#if defined(DIRECT3D12)
        "D3D12",
#endif
#if defined(VULKAN)
        "Vulkan",
#endif
#if defined(DIRECT3D11)
        "D3D11",
#endif
    };

    // Select Api
    DropdownWidget selectApUIWidget = {};
    selectApUIWidget.pData = &gSelectedApiIndex;

    uint32_t apiCount = RENDERER_API_COUNT;
#ifdef DIRECT3D11
    if (gD3D11Unsupported)
    {
        --apiCount;
    }
#endif
    ASSERT(apiCount != 0 && "No supported Graphics API available!");
    selectApUIWidget.pNames = pApiNames;
    selectApUIWidget.mCount = apiCount;

    pSelectApUIWidget = uiCreateComponentWidget(pAPISwitchingComponent, "Select API", &selectApUIWidget, WIDGET_TYPE_DROPDOWN);
    pSelectApUIWidget->pOnEdited = [](void* pUserData)
    {
        UNREF_PARAM(pUserData);
        ResetDesc resetDescriptor{ RESET_TYPE_API_SWITCH };
        requestReset(&resetDescriptor);
    };
    REGISTER_LUA_WIDGET(pSelectApUIWidget);

    static const char* gpuNames[] = { gPlatformParameters.ppAvailableGpuNames[0], gPlatformParameters.ppAvailableGpuNames[1],
                                      gPlatformParameters.ppAvailableGpuNames[2], gPlatformParameters.ppAvailableGpuNames[3] };

    DropdownWidget selectGraphicCardUIWidget = {};
    selectGraphicCardUIWidget.pData = &gPlatformParameters.mSelectedGpuIndex;
    selectGraphicCardUIWidget.pNames = gpuNames;
    selectGraphicCardUIWidget.mCount = gPlatformParameters.mAvailableGpuCount;

    pSelectGraphicCardWidget =
        uiCreateComponentWidget(pAPISwitchingComponent, "Select Graphic Card", &selectGraphicCardUIWidget, WIDGET_TYPE_DROPDOWN);
    pSelectGraphicCardWidget->pOnEdited = [](void* pUserData)
    {
        UNREF_PARAM(pUserData);
        ResetDesc resetDescriptor{ RESET_TYPE_GRAPHIC_CARD_SWITCH };
        requestReset(&resetDescriptor);
    };
    REGISTER_LUA_WIDGET(pSelectGraphicCardWidget);

#if defined(ENABLE_FORGE_SCRIPTING) && defined(AUTOMATED_TESTING)
    // Tests below are executed last, after tests registered in IApp::Init have executed
    const char*    sLastTestScripts[] = { "Test_API_Switching.lua" };
    const uint32_t numScripts = sizeof(sLastTestScripts) / sizeof(sLastTestScripts[0]);
    LuaScriptDesc  scriptDescs[numScripts] = {};
    for (uint32_t i = 0; i < numScripts; ++i)
    {
        scriptDescs[i].pScriptFileName = sLastTestScripts[i];
    }
    luaDefineScripts(scriptDescs, numScripts);
#endif
#endif
}

void togglePlatformUI()
{
    gShowPlatformUI = pApp->mSettings.mShowPlatformUI;

#ifdef ENABLE_FORGE_UI
    extern void platformToggleWindowSystemUI(bool);
    platformToggleWindowSystemUI(gShowPlatformUI);

    uiSetComponentActive(pToggleVSyncComponent, gShowPlatformUI);
    uiSetComponentActive(pAPISwitchingComponent, gShowPlatformUI);
#if defined(ENABLE_FORGE_RELOAD_SHADER)
    uiSetComponentActive(pReloadShaderComponent, gShowPlatformUI);
#endif
#endif
}

//------------------------------------------------------------------------
// APP ENTRY POINT
//------------------------------------------------------------------------

// WindowsWindow.cpp
extern void initWindowClass();
extern void exitWindowClass();

int          IApp::argc;
const char** IApp::argv;

int WindowsMain(int argc, char** argv, IApp* app)
{
    AVBOITBootstrapConfigure(argc, argv, app ? app->GetName() : "unknown");

    AVBOITBootstrapWrite("MEM_ALLOC_INIT_BEGIN");
    if (!initMemAlloc(app->GetName()))
    {
        AVBOITBootstrapWrite("MEM_ALLOC_INIT_FAILED");
        return EXIT_FAILURE;
    }
    AVBOITBootstrapWrite("MEM_ALLOC_INIT_END");

    AVBOITBootstrapWrite("FILESYSTEM_INIT_BEGIN");
    FileSystemInitDesc fsDesc = {};
    fsDesc.pAppName = app->GetName();
    if (!initFileSystem(&fsDesc))
    {
        AVBOITBootstrapWrite("FILESYSTEM_INIT_FAILED");
        return EXIT_FAILURE;
    }
    AVBOITBootstrapWrite("FILESYSTEM_INIT_END");

    fsSetPathForResourceDir(pSystemFileIO, RM_DEBUG, RD_LOG, "");

#if defined(ENABLE_GRAPHICS_DEBUG) && defined(VULKAN) && VK_OVERRIDE_LAYER_PATH
    // We are now shipping validation layer in the repo itself to remove dependency on Vulkan SDK to be installed
    // Set VK_LAYER_PATH to executable location so it can find the layer files that our application wants to use
    SetEnvironmentVariableA("VK_LAYER_PATH", pSystemFileIO->GetResourceMount(RM_DEBUG));
#endif

#ifdef ENABLE_MTUNER
    rmemInit(0);
#endif

    initLog(app->GetName(), DEFAULT_LOG_LEVEL);
    AVBOITBootstrapWrite("FORGE_LOG_INIT_END");

    ULONG majorVersion = 0;
    ULONG minorVersion = 0;
    ULONG buildNumber = 0;
    getOsVersion(majorVersion, minorVersion, buildNumber);
    snprintf(gOsInfo.osName, 256, "Windows PC");
    snprintf(gOsInfo.osVersion, 256, "%lu.%lu (Build: %lu)", majorVersion, minorVersion, buildNumber);
    snprintf(gOsInfo.osDeviceName, 256, "Unknown");
    LOGF(LogLevel::eINFO, "Operating System: %s. Version: %s. Device Name: %s.", gOsInfo.osName, gOsInfo.osVersion, gOsInfo.osDeviceName);

#ifdef ENABLE_FORGE_STACKTRACE_DUMP
    if (!WindowsStackTrace::Init())
        return EXIT_FAILURE;
#endif

    pApp = app;
    pWindowAppRef = app;

    AVBOITBootstrapWrite("COMMAND_LINE_PARSE_BEGIN");
    if (!ParseRendererApiCommandLine(argc, argv))
    {
        AVBOITBootstrapWrite("COMMAND_LINE_PARSE_FAILED");
        return EXIT_FAILURE;
    }
    AVBOITBootstrapWrite("COMMAND_LINE_PARSED");

    initWindowClass();
    AVBOITBootstrapWrite("WINDOW_CLASS_INIT_END");

    // Used for automated testing, if enabled app will exit after DEFAULT_AUTOMATION_FRAME_COUNT (240) frames
#if defined(AUTOMATED_TESTING)
    uint32_t frameCounter = 0;
    uint32_t targetFrameCount = DEFAULT_AUTOMATION_FRAME_COUNT;
#endif

    initCpuInfo(&gCpu);

    IApp::Settings* pSettings = &pApp->mSettings;
    WindowDesc      window = {};
    gWindow = &window;     // WindowsWindow.cpp
    gWindowDesc = &window; // WindowsBase.cpp
    gLogWindowHandle =
        (HWND*)&window.handle
            .window; // WindowsLog.c, save the address to this handle to avoid having to adding includes to WindowsLog.c to use WindowDesc*.

    if (pSettings->mMonitorIndex < 0 || pSettings->mMonitorIndex >= (int)gMonitorCount)
    {
        pSettings->mMonitorIndex = 0;
    }

    if (pSettings->mWidth <= 0 || pSettings->mHeight <= 0)
    {
        RectDesc rect = {};

        getRecommendedResolution(&rect);
        pSettings->mWidth = getRectWidth(&rect);
        pSettings->mHeight = getRectHeight(&rect);
    }

    MonitorDesc* monitor = getMonitor(pSettings->mMonitorIndex);
    ASSERT(monitor != nullptr);

    gWindow->clientRect = { (int)pSettings->mWindowX + monitor->monitorRect.left, (int)pSettings->mWindowY + monitor->monitorRect.top,
                            (int)pSettings->mWidth, (int)pSettings->mHeight };

    gWindow->windowedRect = gWindow->clientRect;
    gWindow->fullScreen = pSettings->mFullScreen;
    gWindow->maximized = false;
    gWindow->noresizeFrame = !pSettings->mDragToResize;
    gWindow->borderlessWindow = pSettings->mBorderlessWindow;
    gWindow->centered = false; // pSettings->mCentered;
    gWindow->forceLowDPI = pSettings->mForceLowDPI;
    gWindow->overrideDefaultPosition = true;
    gWindow->cursorCaptured = false;

    if (!pSettings->mExternalWindow)
        openWindow(pApp->GetName(), gWindow);
    AVBOITBootstrapWrite("WINDOW_OPEN_END");

    pSettings->mWidth = gWindow->fullScreen ? getRectWidth(&gWindow->fullscreenRect) : getRectWidth(&gWindow->clientRect);
    pSettings->mHeight = gWindow->fullScreen ? getRectHeight(&gWindow->fullscreenRect) : getRectHeight(&gWindow->clientRect);

    pApp->pCommandLine = GetCommandLineA();

#ifdef AUTOMATED_TESTING
    char benchmarkOutput[1024] = { "\0" };
    // Check if benchmarking was given through command line
    for (int i = 0; i < argc; i += 1)
    {
        if (strcmp(argv[i], "-b") == 0)
        {
            pSettings->mBenchmarking = true;
            if (i + 1 < argc && isdigit(*argv[i + 1]))
                targetFrameCount = min(max(atoi(argv[i + 1]), 32), 512);
        }
        else if (strcmp(argv[i], "--request-recompile-after") == 0)
        {
            extern uint32_t gReloadServerRequestRecompileAfter;
            if (i + 1 < argc && isdigit(*argv[i + 1]))
                gReloadServerRequestRecompileAfter = atoi(argv[i + 1]);
        }
        // Run forever, this is useful when the app will control when the automated tests are over
        else if (strcmp(argv[i], "--no-auto-exit") == 0)
        {
            targetFrameCount = UINT32_MAX;
        }
        else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc)
        {
            strcpy(benchmarkOutput, argv[i + 1]);
        }
    }
#endif

    {
        AVBOITBootstrapWrite("BASE_SUBSYSTEMS_INIT_BEGIN");
        if (!initBaseSubsystems())
        {
            AVBOITBootstrapWrite("BASE_SUBSYSTEMS_INIT_FAILED");
            return EXIT_FAILURE;
        }
        AVBOITBootstrapWrite("BASE_SUBSYSTEMS_INIT_END");

        Timer t;
        initTimer(&t);
        AVBOITBootstrapWrite("APP_INIT_BEGIN");
        if (!pApp->Init())
        {
            AVBOITBootstrapWrite("APP_INIT_FAILED");
            const char* pRendererReason;
            if (hasRendererInitializationError(&pRendererReason))
            {
                pApp->ShowUnsupportedMessage(pRendererReason);
            }

            if (pApp->mUnsupported)
            {
                errorMessagePopup("Application unsupported", pApp->pUnsupportedReason ? pApp->pUnsupportedReason : "",
                                  &pApp->pWindow->handle, NULL);
                exitLog();
                return 0;
            }

            return EXIT_FAILURE;
        }
        AVBOITBootstrapWrite("APP_INIT_END");

        LOGF(LogLevel::eINFO, "Created Renderer API: %s", RendererApiToString(gPlatformParameters.mSelectedRendererApi));
        if (gPlatformParameters.mAvailableGpuCount > 0 && gPlatformParameters.mSelectedGpuIndex < gPlatformParameters.mAvailableGpuCount)
        {
            LOGF(LogLevel::eINFO, "Selected GPU Name: %s", gPlatformParameters.ppAvailableGpuNames[gPlatformParameters.mSelectedGpuIndex]);
        }
        if (gCommandLineRendererApiRequested && gPlatformParameters.mSelectedRendererApi != gCommandLineRendererApi)
        {
            LOGF(eERROR, "Requested Renderer API %s but created %s.", RendererApiToString(gCommandLineRendererApi),
                 RendererApiToString(gPlatformParameters.mSelectedRendererApi));
            AVBOITBootstrapWrite("RENDERER_API_MISMATCH");
            return EXIT_FAILURE;
        }

        setupPlatformUI(pSettings);
        pSettings->mInitialized = true;

        AVBOITBootstrapWrite("APP_LOAD_BEGIN");
        if (!pApp->Load(&gReloadDescriptor))
        {
            AVBOITBootstrapWrite("APP_LOAD_FAILED");
            return EXIT_FAILURE;
        }
        AVBOITBootstrapWrite("APP_LOAD_END");

        LOGF(LogLevel::eINFO, "Application Init+Load+Reload %fms", getTimerMSec(&t, false) / 1000.0f);
    }

#ifdef AUTOMATED_TESTING
    if (pSettings->mBenchmarking)
        setAggregateFrames(targetFrameCount / 2);
#endif

    bool    baseSubsystemAppDrawn = false;
    bool    quit = false;
    int64_t lastCounter = getUSec(false);
    AVBOITBootstrapWrite("FRAME_LOOP_BEGIN");
    while (!quit)
    {
        int64_t counter = getUSec(false);
        float   deltaTime = CounterToSecondsElapsed(lastCounter, counter);
        lastCounter = counter;

#ifdef FORGE_DEBUG
        // if framerate appears to drop below about 6, assume we're at a breakpoint and simulate 20fps.
        if (deltaTime > 0.15f)
            deltaTime = 0.05f;
#endif

#if defined(AUTOMATED_TESTING)
        // Used to keep screenshot results consistent across CI runs
        deltaTime = AUTOMATION_FIXED_FRAME_TIME;
#endif

        bool lastMinimized = gWindow->minimized;

        extern bool handleMessages();
        quit = handleMessages() || pSettings->mQuit;

        // UPDATE BASE INTERFACES
        updateBaseSubsystems(deltaTime, baseSubsystemAppDrawn);
        baseSubsystemAppDrawn = false;

        if (gResetDescriptor.mType != RESET_TYPE_NONE)
        {
            if (gResetDescriptor.mType & RESET_TYPE_DEVICE_LOST)
            {
                errorMessagePopup(
                    "Graphics Device Lost",
                    "Connection to the graphics device has been lost.\nPlease verify the integrity of your graphics drivers.\nCheck the "
                    "logs for further details.",
                    &pApp->pWindow->handle, NULL);
            }

            if (gResetDescriptor.mType & RESET_TYPE_GRAPHIC_CARD_SWITCH)
            {
                ASSERT(gPlatformParameters.mSelectedGpuIndex < gPlatformParameters.mAvailableGpuCount);
                gPlatformParameters.mPreferedGpuId = gPlatformParameters.pAvailableGpuIds[gPlatformParameters.mSelectedGpuIndex];
            }

            gReloadDescriptor.mType = RELOAD_TYPE_ALL;
            pApp->Unload(&gReloadDescriptor);
            pApp->Exit();

            gPlatformParameters.mSelectedRendererApi = (RendererApi)gSelectedApiIndex;
            pSettings->mInitialized = false;

            closeWindow(app->pWindow);
            openWindow(app->GetName(), app->pWindow);

            exitBaseSubsystems();

            {
                if (!initBaseSubsystems())
                    return EXIT_FAILURE;

                Timer t;
                initTimer(&t);
                if (!pApp->Init())
                {
                    if (pApp->mUnsupported)
                    {
                        errorMessagePopup("Application unsupported", pApp->pUnsupportedReason ? pApp->pUnsupportedReason : "",
                                          &pApp->pWindow->handle, NULL);
                        exitLog();
                        return 0;
                    }
                    return EXIT_FAILURE;
                }

                setupPlatformUI(pSettings);
                pSettings->mInitialized = true;

                if (!pApp->Load(&gReloadDescriptor))
                    return EXIT_FAILURE;

                LOGF(LogLevel::eINFO, "Application Reset %fms", getTimerMSec(&t, false) / 1000.0f);
            }

            gResetDescriptor.mType = RESET_TYPE_NONE;
            continue;
        }

        if (gReloadDescriptor.mType != RELOAD_TYPE_ALL)
        {
            Timer t;
            initTimer(&t);

            pApp->Unload(&gReloadDescriptor);
            if (!pApp->Load(&gReloadDescriptor))
                return EXIT_FAILURE;

            LOGF(LogLevel::eINFO, "Application Reload %fms", getTimerMSec(&t, false) / 1000.0f);
            gReloadDescriptor.mType = RELOAD_TYPE_ALL;
            continue;
        }

        // If window is minimized let other processes take over
        if (gWindow->minimized)
        {
            // Call update once after minimize so app can react.
            if (lastMinimized != gWindow->minimized)
            {
                pApp->Update(deltaTime);
            }
            threadSleep(1);
            continue;
        }

        // UPDATE APP
        pApp->Update(deltaTime);
        pApp->Draw();
        baseSubsystemAppDrawn = true;

        if (gShowPlatformUI != pApp->mSettings.mShowPlatformUI)
        {
            togglePlatformUI();
        }
#if defined(ENABLE_FORGE_RELOAD_SHADER)
        if (platformReloadClientShouldQuit())
            quit = true;
#endif

#ifdef AUTOMATED_TESTING
        extern bool gAutomatedTestingScriptsFinished;
        // wait for the automated testing if it hasn't managed to finish in time
        if (gAutomatedTestingScriptsFinished && frameCounter >= targetFrameCount)
            quit = true;
        frameCounter++;
#endif
    }

#ifdef AUTOMATED_TESTING
    if (pSettings->mBenchmarking)
    {
        dumpBenchmarkData(pSettings, benchmarkOutput, pApp->GetName());
        dumpProfileData(benchmarkOutput, targetFrameCount);
    }
#endif

    gReloadDescriptor.mType = RELOAD_TYPE_ALL;
    pApp->mSettings.mQuit = true;
    AVBOITBootstrapWrite("APP_UNLOAD_BEGIN");
    pApp->Unload(&gReloadDescriptor);
    pApp->Exit();
    AVBOITBootstrapWrite("APP_UNLOAD_END");

    exitWindowClass();

#ifdef ENABLE_FORGE_STACKTRACE_DUMP
    WindowsStackTrace::Exit();
#endif

    exitLog();

    exitBaseSubsystems();

    exitFileSystem();

#ifdef ENABLE_MTUNER
    rmemUnload();
    rmemShutDown();
#endif

    exitMemAlloc();

    gWindow = NULL;
    gWindowDesc = NULL;
    gLogWindowHandle = NULL;
    AVBOITBootstrapClose();
    return 0;
}
#endif
