@echo off

set "keep1=clone and decode.bat"
set "keep2=encryption_key.key"
set "keep3=clean.bat"
set "keep4=venv"

REM Loop through all files in the current directory
for %%f in (*) do (
    if /i not "%%f"=="%keep1%" if /i not "%%f"=="%keep2%" if /i not "%%f"=="%keep3%" if /i not "%%f"=="%keep4%" (
        echo Deleting file: %%f
        del "%%f"
    ) else (
        echo Keeping file: %%f
    )
)

REM Remove hidden attribute from .git and delete all directories in the current directory
attrib -h -s .git 2>nul
for /d %%d in (*) do (
    if /i not "%%d"==".git" if /i not "%%d"=="venv" (
        echo Deleting directory: %%d
        rd /s /q "%%d"
    ) else (
        echo Keeping directory: %%d
    )
)