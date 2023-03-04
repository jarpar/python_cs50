import re

url = input("URL: ").strip()

# username = url.replace("http?s://\.twitter.com/", "")
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/?", "", url)

# test input:
# https://twitter.com/user_name1
if matches := re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE
):
    # added test for polish special characters:
    #     r"^https?://(?:www\.)?twitter\.com/([a-z0-9_\.ą-ż]+)", url, re.IGNORECASE
    # ):
    print(f"Username: ", matches.group(1))

