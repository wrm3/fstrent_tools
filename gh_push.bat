@echo off
echo GitHub Push Utility

REM Get current version before any operations
for /f "tokens=3" %%i in ('findstr /B "current_version =" .bumpversion.cfg') do set INITIAL_VERSION=%%i
echo Current version before any operations: v%INITIAL_VERSION%

REM Get the bump type and commit message
set /p BUMP_TYPE="Enter bump type (major/minor/patch) or none: "
set /p MESSAGE="Enter commit message: "

REM Stage all changes
git add .

REM If we're not bumping version, just commit and push
if "%BUMP_TYPE%"=="none" (
    git commit -m "%MESSAGE%"
) else (
    REM Commit current changes first
    git commit -m "%MESSAGE%"
    
    REM Get current version before bump
    for /f "tokens=3" %%i in ('findstr /B "current_version =" .bumpversion.cfg') do set OLD_VERSION=%%i
    echo Current version before bump: v%OLD_VERSION%
    
    REM Check PyPI version
    for /f "tokens=2 delims=() " %%i in ('pip index versions fstrent_tools ^| findstr /R /C:"^fstrent_tools ("') do set PYPI_VERSION=%%i
    echo Current version on PyPI: v%PYPI_VERSION%
    
    REM Verify we're not trying to bump from a version that's behind PyPI
    if "%OLD_VERSION%"=="%PYPI_VERSION%" (
        REM Now do the version bump (working directory will be clean)
        echo Bumping %BUMP_TYPE% version from v%OLD_VERSION%...
        python -m bumpversion %BUMP_TYPE%
        
        REM Get new version after bump
        for /f "tokens=3" %%i in ('findstr /B "current_version =" .bumpversion.cfg') do set NEW_VERSION=%%i
        echo Version bumped: v%OLD_VERSION% -^> v%NEW_VERSION%
    ) else (
        echo ERROR: Local version v%OLD_VERSION% does not match PyPI version v%PYPI_VERSION%
        echo Please sync versions before continuing
        exit /b 1
    )
)

REM Push to main branch with tags
git push origin main --tags

echo Done!
pause
