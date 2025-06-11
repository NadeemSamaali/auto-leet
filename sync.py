import requests
import os
import tempfile

# Leetcode user information
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")

# Headers
headers = {
    "cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};",
    "x-csrftoken": CSRFTOKEN,
    "referer": "https://leetcode.com/submissions/",
    "User-Agent": "Mozilla/5.0"
}

# User proxies if necessary
proxies = {
    "http":"",
    "https":"",
}

def get_submission_metadata(sub) : 
    dir_header = f'{sub["question_id"]}-{sub["title_slug"]}'
    commit_message = f'Runtime : {sub["runtime"]} | Memory : {sub["memory"]}'
    language = sub["lang_name"]
    code = sub["code"]

    return {"dir_header" : dir_header,
            "code" : code,
            "commit_message" : commit_message,
            "language" : language
            }

# Pagination
offset = 0
limit = 10
has_next = True
fetched_submissions = []

seen_problems = set()  # keep track of problems with accepted submissions found

while has_next:
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        print("Failed to fetch submissions:", response.status_code)
        print(response.text)
        continue

    data = response.json()
    submissions = data.get("submissions_dump", [])

    for sub in submissions:
        slug = sub["title_slug"]
        if sub["status_display"] == "Accepted" and slug not in seen_problems:
            seen_problems.add(slug)

            fetched_submissions.append(get_submission_metadata(sub))

    has_next = data.get("has_next", False)
    offset += limit

class git_handler : 

    def __init__(self) :
        # Github user information
        GIT_PAT = os.getenv("GIT_PAT")
        REPO_URL = os.getenv("REPO_URL")

        repo_name = REPO_URL.split("/")[-1]
        repo_owner = REPO_URL.split("/")[-2]

        git_url = f'https://{GIT_PAT}:x-oauth-basic@github.com/{repo_owner}/{repo_name}.git'        

