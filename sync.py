import requests

# User information
LEETCODE_SESSION = ""
CSRFTOKEN = ""

# Request Header
headers = {
    "cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};",
    "x-csrfroken": CSRFTOKEN,
    "referer": f"https://leetcode.com/problems/{slug}",
    "User-Agent": "Mozilla/5.0"
}

# User proxies if necessary
proxies = {
    "http":"",
    "https":"",
}

# Pagination
offset = 0
limit = 20
has_next = True

seen_problems = set()  # keep track of problems with accepted submissions found

while has_next:
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        print("Failed to fetch submissions:", response.status_code)
        print(response.text)
        break

    data = response.json()
    submissions = data.get("submissions_dump", [])

    for sub in submissions:
        slug = sub["title_slug"]
        if sub["status_display"] == "Accepted" and slug not in seen_problems:
            seen_problems.add(slug)

            print("=== Most Recent Accepted Submission ===")
            print("Title:", sub["title"])
            print("Slug:", slug)
            print("Language:", sub["lang"])
            print("Timestamp:", sub["timestamp"])
            print("Code:\n", sub["code"])
            print("=" * 40)

    has_next = data.get("has_next", False)
    offset += limit