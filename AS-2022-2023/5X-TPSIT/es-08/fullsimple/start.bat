@echo off
REM file: start.bat
cd %~dp0
REM accoda altri parametri ES: --no-use-colors
set PARAM=%1%
set FILE=webapp
set APP=webapp
REM Imposta HOST=<TUO_IP>
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr IPv4') do set HOST=%%a
set PORT=80
set PYTHON=python
set BROWSER="C:\Program Files\Vivaldi\Application\vivaldi.exe"

:updatingchecking
CLS
REM *** Controllo esistenza dei moduli necessari ***
echo Check packages..
setlocal
set modules=httptools uvicorn fastapi jinja2
for %%i in (%modules%) do (
	%PYTHON% -m pip show %%i >nul 2>&1
	if errorlevel 1 (
		echo [%%i] not found, installing..
		%PYTHON% -m pip install %%i
	) else (
		echo [%%i] already installed..
	)
)
endlocal

:browserlaunching
REM *** Apre il browser ***
%BROWSER% "http://%HOST:~1%:%PORT%/"

:startfastapi
REM *** Avvia FastAPI ***
%PYTHON% -m uvicorn %FILE%:%APP% --reload --host 0.0.0.0 --port %PORT% --http httptools %PARAM%
