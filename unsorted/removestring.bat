@echo off
:load
set /p file="Set Input File Name (without extension): "
if "%file%" == "q" (goto end)
:start
set /p search="String to remove: "
if "%search%" == "q" (goto load)
ren %file%.txt tempfile.txt
find /i /v "%search%" < tempfile.txt > %file%.txt
del tempfile.txt
echo %search% removed from %file%
goto start
:end