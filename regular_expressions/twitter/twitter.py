import re
url = input("URL: ").strip()

# username = url.replac("https://twitter.com/", "")
username = re.sub(r"^http?s://twitter\.com/", "", url)

print(f"Username: {username}")
