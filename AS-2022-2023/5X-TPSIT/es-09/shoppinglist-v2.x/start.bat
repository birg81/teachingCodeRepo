@echo off
REM file: start.bat
cd %~dp0
CLS

:configuring
REM remove old cache
rmdir /s /q .\__pycache__
REM append other missing parameters Ex: --no-use-colors
set PARAM=%1%
set FILE=shopapp
set APP=webapp
REM Imposta HOST=<TUO_IP>
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr IPv4') do set HOST=%%a
REM default HTTP port
set PORT=80
REM your default python interpeter
set PYTHON=python

REM skip modules checking
goto browserlaunching

:updatingchecking
REM *** checked and install your missing python modules ***
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
REM Launch your browser in your local IP
set BROWSER="C:\Program Files\Vivaldi\Application\vivaldi.exe"
%BROWSER% "http://%HOST:~1%:%PORT%/"

:startfastapi
REM *** start your FastAPI app ***
%PYTHON% -m uvicorn %FILE%:%APP% --reload --host 0.0.0.0 --port %PORT% --http httptools %PARAM%