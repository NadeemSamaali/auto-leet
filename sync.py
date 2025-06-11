import requests
import os
import tempfile
from pathlib import Path
from git import Repo

# Github user information
GIT_PAT = os.getenv("GIT_PAT")
REPO_URL = os.getenv("REPO_URL")

repo_name = REPO_URL.split("/")[-1]
repo_owner = REPO_URL.split("/")[-2]

git_url = f'https://{GIT_PAT}:x-oauth-basic@github.com/{repo_owner}/{repo_name}'

# Clone repo into a temporary directory
temp_dir = tempfile.TemporaryDirectory()
temp_path = Path(temp_dir.name)
repo = Repo.clone_from(git_url, temp_path)

# Read repo files into memory
file_map = {}
for file in temp_path.rglob("*") :
    if file.is_file() and ".git" not in file.parts:
        rel_path = str(file.relative_to(temp_path))
        file_map[rel_path] = file.read_text(encoding="utf8")

# Leetcode user information
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")

# Leetcode Headers
headers = {
    "cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};",
    "x-csrftoken": CSRFTOKEN,
    "referer": "https://leetcode.com/submissions/",
    "User-Agent": "Mozilla/5.0"
}

# User proxies if necessary
proxies = {
    "http": os.getenv("HTTP_PROXY"),
    "https": os.getenv("HTTPS_PROXY"),
}

leetcode_lang_to_ext = {
    "cpp": ".cpp",
    "java": ".java",
    "python": ".py",
    "python3": ".py",
    "c": ".c",
    "csharp": ".cs",
    "javascript": ".js",
    "typescript": ".ts",
    "php": ".php",
    "swift": ".swift",
    "kotlin": ".kt",
    "dart": ".dart",
    "golang": ".go",
    "scala": ".scala",
    "rust": ".rs",
    "ruby": ".rb",
    "mysql": ".sql",
    "mssql": ".sql",
    "oraclesql": ".sql",
    "bash": ".sh",
    "racket": ".rkt",
    "erlang": ".erl",
    "elixir": ".ex",
    "haskell": ".hs",
    "perl": ".pl",
    "lua": ".lua",
    "clojure": ".clj",
    "fsharp": ".fs",
    "vb": ".vb",
    "julia": ".jl",
    "scheme": ".scm",
    "groovy": ".groovy",
    "pascal": ".pas",
    "assembly": ".asm"
}

def get_submission_metadata(sub) : 
    dir_header = f'{sub["question_id"]}-{sub["title_slug"]}/{sub["title_slug"]}-{sub["timestamp"]}{leetcode_lang_to_ext[sub["lang"]]}'
    commit_message = f'Runtime : {sub["runtime"]} | Memory : {sub["memory"]}'
    code = sub["code"]
    id = int(sub["question_id"])

    return {"id": id,
            "dir" : dir_header,
            "code" : code,
            "commit_message" : commit_message
            }

# Pagination
offset = 0
limit = 10
has_next = True
fetched_submissions = []

#seen_problems = set()  # keep track of problems with accepted submissions found

while has_next:
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        continue

    data = response.json()
    submissions = data.get("submissions_dump", [])

    for sub in submissions:
        slug = sub["title_slug"]
        if sub["status_display"] == "Accepted" : #and slug not in seen_problems:
            #seen_problems.add(slug)
            fetched_submissions.append(get_submission_metadata(sub))

    has_next = data.get("has_next", False)
    offset += limit

fetched_submissions = sorted(fetched_submissions, key=lambda x: x["id"])
print(fetched_submissions)

# Commiting each file separately         
for sub in fetched_submissions :
    rel_path = sub["dir"]
    content = sub["code"]
    commit_message = sub["commit_message"]

    file_path = temp_path / rel_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")

    repo.git.add(rel_path)
    repo.index.commit(commit_message)
    # Push
    repo.remote().push()

# Clean up locks to avoid PermissionError
repo.close()
temp_dir.cleanup()