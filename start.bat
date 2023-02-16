@echo off
@setlocal enableextensions
@cd /d "%~dp0"
python main.py -no_errors textures -file test2.txt -parse -overwrite
pause