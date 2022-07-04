@echo off

call %CONDA_PATH%\Scripts\activate.bat %CONDA_PATH%
python move.py

pause
