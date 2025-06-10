import requests

# User information
LEETCODE_SESSION = ""
CSRFTOKEN = ""
slug = ""

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

# Request
url = f"https://leetcode.com/api/submissions/{slug}/"
response = requests.get(url, headers=headers, proxies=proxies)
data = response.json()

if response.status_code == 200:
    data = response.json()
    for sub in data["submissions_dump"]:
        if sub["status_display"] == "Accepted":
            print("Found Accepted Submission")
            print("Language:", sub["lang"])
            print("Code:\n", sub["code"])
            break
else:
    print("Failed:", response.status_code)
    print(response.text)