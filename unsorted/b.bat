@echo off
:load
set /p file="Set Input File Name (without extension or dan_): "
if "%file%" == "q" (goto end)
:start
set /p search="String to remove: "
if "%search%" == "q" (goto load)
ren dan_%file%.txt dan_tempfile.txt
find /i /v "%search%" < dan_tempfile.txt > dan_%file%.txt
del dan_tempfile.txt
echo %search% removed from dan_%file%
goto start
:end