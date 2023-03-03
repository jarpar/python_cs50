import re

email = input("What's your email? ").strip()

if re.search(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email
):
    print("Valid")
else:
    print("Invalid")
