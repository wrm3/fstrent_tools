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
    
    REM Now do the version bump (working directory will be clean)
    echo Bumping %BUMP_TYPE% version...
    python -m bumpversion %BUMP_TYPE%
)

REM Push to main branch with tags
git push origin main --tags

echo Done!
pause
