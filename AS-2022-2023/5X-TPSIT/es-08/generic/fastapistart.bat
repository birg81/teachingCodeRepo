@echo off
REM file: fastapistart.bat
cd %~dp0
CLS
REM *** Envairoment VAR SETTING ***
REM accoda altri parametri ES: --no-use-colors
set PARAM=%1%
REM module name / file name
set FASTAPI_FILE=webapp
REM app is file: 'webapp.py'. this file contains routing
set FASTAPI_APP=webapp
REM development mode (print PIN for edit with python on browser)
set FASTAPI_ENV=development
REM Host address setting - 0.0.0.0 so you can open from other device too
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr IPv4') do set HOST=%%a
REM PORT setting
set FASTAPI_RUN_PORT=80
REM set your favorite browser in my case Vivaldi
set BROWSER="C:\Program Files\Vivaldi\Application\vivaldi.exe"
REM set your python path
set PYTHON=python

REM bypass updating checking
goto :browserlaunch

:update
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

:browserlaunch
REM Start web page in your browser after lauch this file
%BROWSER% "http://%HOST:~1%:%FASTAPI_RUN_PORT%"
:runfastapi
REM *** Start FastAPI ***
%PYTHON% -m uvicorn %FASTAPI_FILE%:%FASTAPI_APP% --reload --host 0.0.0.0 --port %FASTAPI_RUN_PORT% --http httptools %PARAM%