@echo off
@setlocal enableextensions
@cd /d "%~dp0"
env\Scripts\python main.py -no_errors textures -file main.log -parse -overwrite
pause