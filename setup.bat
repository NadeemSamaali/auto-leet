REM     FOR WINDOWS SYSTEMS

@echo off
REM Exporting environment variables
echo Exporting environment variables
set "LEETCODE_SESSION="
set "CSRFTOKEN="
set "GIT_PAT="

REM Make sure the repo URL contains .git at the end
set "REPO_URL="

REM Proxy configuration if necessary -- Leave blank if not needed
echo Setting up proxy
set "HTTP_PROXY="
set "HTTPS_PROXY="

echo Running sync.py
python sync.py
