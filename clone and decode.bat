@echo off
git clone https://creditoltd.visualstudio.com/Credito.Algorithms/_git/DBQueries temp_folder
xcopy temp_folder\* . /E /H /Y
rmdir /S /Q temp_folder

if not exist venv call venv.bat
if exist venv call venv\Scripts\activate

python decode.py
