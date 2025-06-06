@REM read all files in directory created after given date
@echo off
setlocal enabledelayedexpansion
set "dirPath=%~1"
set "dateFilter=%~2"
if "%dirPath%"=="" (
    echo Usage: readDirFiles.bat ^<directory^> ^<date^>
    exit /b 1
)
if "%dateFilter%"=="" (
    echo Usage: readDirFiles.bat ^<directory^> ^<date^>
    exit /b 1
)
if not exist "%dirPath%" (
    echo Directory "%dirPath%" does not exist.
    exit /b 1
)
rem Expecting dateFilter as YYYY-MM-DD, convert to YYYYMMDD for comparison
set "dateFilter=!dateFilter:~0,4!!dateFilter:~5,2!!dateFilter:~8,2!"

for /f "delims=" %%F in ('dir /b /a-d "%dirPath%"') do (
    set "filePath=%dirPath%\%%F"
    for /f %%D in ('wmic datafile where "name='!filePath:\=\\!'" get creationdate ^| findstr /r "^[0-9]"') do (
        set "fileDate=%%D"
        set "fileDate=!fileDate:~0,8!"
        if "!fileDate!" gtr "!dateFilter!" (
            echo %%F
        )
    )
)