@echo off
setlocal enabledelayedexpansion

REM Spec Agent Installer for Claude Code CLI (Windows)
REM 汎用仕様書作成Agent群のインストーラー

echo ============================================================
echo Spec Agent Installer for Claude Code CLI
echo 汎用仕様書作成Agent群 インストーラー
echo OS: Windows
echo ============================================================

REM Claude Code確認
where claude >nul 2>&1
if %errorlevel% equ 0 (
    echo [✓] Claude Code CLI が検出されました
) else (
    echo [×] Claude Code CLI が見つかりません
    echo    以下のコマンドでインストールしてください:
    echo    npm install -g @anthropic-ai/claude-code
    pause
    exit /b 1
)

REM Python確認
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo [✓] Python が検出されました
    echo.
    echo Pythonインストーラーを実行します...
    python "%~dp0install.py"
) else (
    where py >nul 2>&1
    if %errorlevel% equ 0 (
        echo [✓] Python が検出されました
        echo.
        echo Pythonインストーラーを実行します...
        py "%~dp0install.py"
    ) else (
        echo [×] Python が見つかりません
        echo.
        echo 手動インストールを実行します...
        goto :manual_install
    )
)

goto :end

:manual_install
echo.
echo インストールタイプを選択してください:
echo 1. ユーザーレベル（このユーザー専用）
echo 2. プロジェクトレベル（現在のプロジェクトのみ）
echo.

set /p choice="選択 (1 or 2): "

if "%choice%"=="1" (
    set INSTALL_TYPE=user
    set INSTALL_PATH=%USERPROFILE%\.claude\agents\spec-agent
) else if "%choice%"=="2" (
    set INSTALL_TYPE=project
    set INSTALL_PATH=%CD%\.claude\agents
) else (
    echo 無効な選択です。
    pause
    exit /b 1
)

echo.
echo インストール先: %INSTALL_PATH%

REM 既存インストール確認
if exist "%INSTALL_PATH%" (
    set /p overwrite="既にインストールされています。上書きしますか？ (y/n): "
    if /i not "!overwrite!"=="y" (
        echo インストールをキャンセルしました。
        pause
        exit /b 0
    )
    rmdir /s /q "%INSTALL_PATH%"
)

REM ディレクトリ作成
mkdir "%INSTALL_PATH%" 2>nul
mkdir "%INSTALL_PATH%\templates" 2>nul

echo.
echo ファイルをコピー中...

REM エージェントファイルコピー
for %%f in (
    spec-master-agent.md
    requirement-analyst-agent.md
    system-architect-agent.md
    implementation-spec-agent.md
    technical-writer-agent.md
    qa-reviewer-agent.md
    coordination_rules.yaml
) do (
    if exist "%~dp0%%f" (
        copy /y "%~dp0%%f" "%INSTALL_PATH%\" >nul
        echo   [✓] %%f
    ) else (
        echo   [!] %%f が見つかりません
    )
)

REM テンプレートファイルコピー
for %%f in (progress.md todo.md) do (
    if exist "%~dp0%%f" (
        copy /y "%~dp0%%f" "%INSTALL_PATH%\templates\" >nul
        echo   [✓] templates\%%f
    )
)

REM 設定ファイル作成
echo.
echo 設定ファイルを作成中...

(
echo {
echo   "name": "spec-agent",
echo   "version": "1.0.0",
echo   "type": "%INSTALL_TYPE%",
echo   "description": "汎用仕様書作成Agent群",
echo   "agents": {
echo     "spec-master": {
echo       "file": "spec-master-agent.md",
echo       "description": "仕様書作成プロセス全体を管理"
echo     },
echo     "requirement-analyst": {
echo       "file": "requirement-analyst-agent.md",
echo       "description": "要求分析専門"
echo     },
echo     "system-architect": {
echo       "file": "system-architect-agent.md",
echo       "description": "システム設計専門"
echo     },
echo     "implementation-spec": {
echo       "file": "implementation-spec-agent.md",
echo       "description": "実装仕様専門"
echo     },
echo     "technical-writer": {
echo       "file": "technical-writer-agent.md",
echo       "description": "ドキュメント整形専門"
echo     },
echo     "qa-reviewer": {
echo       "file": "qa-reviewer-agent.md",
echo       "description": "品質レビュー専門"
echo     }
echo   },
echo   "templates": {
echo     "progress": "templates/progress.md",
echo     "todo": "templates/todo.md"
echo   },
echo   "rules": "coordination_rules.yaml"
echo }
) > "%INSTALL_PATH%\spec-agent-config.json"

echo [✓] 設定ファイル作成完了

REM アクティベーション設定
if "%INSTALL_TYPE%"=="user" (
    set CONFIG_DIR=%APPDATA%\claude-code
    set CONFIG_FILE=!CONFIG_DIR!\config.json
) else (
    set CONFIG_DIR=%CD%\.claude
    set CONFIG_FILE=!CONFIG_DIR!\project.json
)

if not exist "!CONFIG_DIR!" mkdir "!CONFIG_DIR!"

if "%INSTALL_TYPE%"=="user" (
    (
    echo {
    echo   "agents": {
    echo     "spec-agent": {
    echo       "path": "%INSTALL_PATH:\=\\%",
    echo       "enabled": true
    echo     }
    echo   }
    echo }
    ) > "!CONFIG_FILE!"
) else (
    (
    echo {
    echo   "name": "%~nx0",
    echo   "agents": {
    echo     "spec-agent": {
    echo       "path": "./agents",
    echo       "enabled": true
    echo     }
    echo   }
    echo }
    ) > "!CONFIG_FILE!"
)

echo [✓] 設定をアクティベートしました

:end
echo.
echo ============================================================
echo [✓] インストール完了！
echo.
echo 使用方法:
echo 1. Claude Codeを起動: claude
echo 2. 以下のコマンドでAgent を呼び出し:
echo    @spec-master-agent プロジェクトを開始します
echo.
echo 詳細は manual.md を参照してください。
echo ============================================================
echo.
pause