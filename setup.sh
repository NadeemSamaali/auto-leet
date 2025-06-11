#   FOR LINUX SYSTEMS

# Exporting environment variables
echo "Exporting environment variables"
export LEETCODE_SESSION=""
export CSRFTOKEN=""
export GIT_PAT=""
export REPO_URL="" # Make sure the repo URL contains .git at the end

# Proxy configuration if necessary -- Leave blank if not needed
echo "Setting up proxy"
export HTTP_PROXY=""
export HTTPS_PROXY=""

echo "Running sync.py"
python sync.py