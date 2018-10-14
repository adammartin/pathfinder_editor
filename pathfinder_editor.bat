:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

python src\pathfinder_editor\pathfinder_editor.py

goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
