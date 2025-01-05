@echo off
echo GitHub Push Utility

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
    for /f "tokens=3 delims= " %%i in ('findstr "current_version" .bumpversion.cfg') do set OLD_VERSION=%%i
    
    REM Now do the version bump (working directory will be clean)
    echo Bumping %BUMP_TYPE% version from v%OLD_VERSION%...
    python -m bumpversion %BUMP_TYPE%
    
    REM Get new version after bump
    for /f "tokens=3 delims= " %%i in ('findstr "current_version" .bumpversion.cfg') do set NEW_VERSION=%%i
    echo Version bumped: v%OLD_VERSION% -^> v%NEW_VERSION%
)

REM Push to main branch with tags
git push origin main --tags

echo Done!
pause
