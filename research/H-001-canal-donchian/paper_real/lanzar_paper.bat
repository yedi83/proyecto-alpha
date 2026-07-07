@echo off
REM ================================================================
REM  Lanzador del PAPER-REAL: precios REALES de mainnet, SIN dinero.
REM  DRY_RUN=true + sin API keys -> no puede colocar ordenes. Cero riesgo.
REM  Reinicia el bot si se cierra/crashea. Ctrl+C dos veces / cerrar para abortar.
REM  Usa %~dp0 (ruta del propio .bat) para no depender de codificacion.
REM ================================================================
set "BOTDIR=%~dp0bot"
set "PY=D:\ESTRATEGIA_ALEX\crypto_iid_rango\.venv\Scripts\python.exe"
if not exist "%PY%" (
    echo ERROR: no se encuentra el python del venv en: %PY%
    echo Edita este .bat y corrige la ruta PY.
    exit /b 1
)
if not exist "%BOTDIR%\logs" mkdir "%BOTDIR%\logs"
:loop
echo %date% %time% LANZADOR_INICIO>> "%BOTDIR%\logs\bot.log"
"%PY%" "%BOTDIR%\live_bot.py"
echo %date% %time% LANZADOR_REINICIO codigo=%errorlevel%>> "%BOTDIR%\logs\bot.log"
REM sleep ~15s headless-safe (timeout falla bajo el Programador; ping no)
ping -n 16 127.0.0.1 >nul
goto loop
