@echo off
setlocal

set /p file=Enter the file name to search:

if not exist %file% (
    echo File not found.
    goto end
)

:loop
set /p input=Enter the search string (enter "q" to quit): 
if "%input%"=="q" (
    echo Exiting...
    goto end
)

set output=split_%input%.txt

echo Searching for "%input%" in file %file%...

findstr /i "%input%" %file% > %output%

echo Search complete. Results saved to %output%.

goto loop

:end
pause
