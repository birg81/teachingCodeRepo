@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
ECHO Cache cleaning in progress...
SET "target=__pycache__"
FOR /R %%i IN (!target!) DO (
	IF EXIST "%%i" (
		ECHO Remove Directory: %%i
		RD /S /Q "%%i"
	)
)
ECHO Completely cleaned...
PAUSE