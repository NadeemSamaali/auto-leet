# AutoLeet : Leetcode to GitHub synchronization tool

This repository automatically syncs your accepted LeetCode submissions to GitHub, organizing them by problem ID and including problem descriptions.

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Edit the setup file** for your OS:
   - Linux/macOS: `setup.sh`
   - Windows: `setup.bat`

3. **Fill in your credentials**:
    
   `setup.sh` :
   ```bash
   # LeetCode
   export LEETCODE_SESSION="your_session_cookie"
   export CSRFTOKEN="your_csrf_token"
   
   # GitHub
   export GIT_PAT="your_github_personal_access_token"
   export REPO_URL="https://github.com/yourusername/yourrepo.git"
   ```

   `setup.bat` :
   ```bat
   @echo off
   REM LeetCode
   set "LEETCODE_SESSION=your_session_cookie"
   set "CSRFTOKEN=your_csrf_token"

   REM GitHub
   set "GIT_PAT=your_github_personal_access_token"
   set "REPO_URL=https://github.com/yourusername/yourrepo.git"
   ```

4. **Run it!**  
   Linux/macOS:
   ```bash
   chmod +x setup.sh && ./setup.sh
   ```
   
   Windows:
   ```bat
   setup.bat
   ```

That's it! Your LeetCode solutions will appear in the repo organized by problem.

## What Gets Synced?

✅ All accepted submissions  
✅ Preserved runtime/memory stats  
✅ Problem descriptions in READMEs  
✅ Supports 25+ programming languages  

## File Structure

```
├── 0001-two-sum/
│   ├── two-sum-1234567890.py
│   └── README.md
├── 0002-add-two-numbers/
│   ├── add-two-numbers-1234567891.java
│   └── README.md
└── ...
```

## Need Help?

1. **Get LeetCode cookies**:
   - Log in to LeetCode
   - Open DevTools (F12) → Application → Cookies
   - Copy `LEETCODE_SESSION` and `csrftoken` values

2. **Create GitHub PAT**:
   - Settings → Developer settings → Personal Access Tokens
   - Select `repo` permissions

3. **Proxy issues?**  
   Set these in the setup file if needed:
   
   `setup.sh` :
   ```bash
   export HTTP_PROXY="your_proxy"
   export HTTPS_PROXY="your_proxy"
   ```

   `setup.bat` :
   ```bat
   echo Setting up proxy
   set "HTTP_PROXY=your_proxy"
   set "HTTPS_PROXY=your_proxy"
   ```

---

💡 **Pro Tip**: Run this weekly to keep your solutions backed up!
