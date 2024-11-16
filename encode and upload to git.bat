call venv\Scripts\activate
python encode.py
git add .
git commit
git push
call clean.bat
del /F /Q "clean.bat" 2>nul
