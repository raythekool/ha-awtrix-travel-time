@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
where python >nul 2>nul
if errorlevel 1 (
    echo Errore: Python non e' installato o non e' disponibile nel PATH.
    exit /b 1
)

python "%SCRIPT_DIR%upload_icons.py" %*