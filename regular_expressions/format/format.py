import re

name = input("What's your name? ").strip()
# := is called "walrus" operator
# The walrus operator is a new syntax that is only available in Python 3.8 and later.
if matches := re.search(r"^(.+), (.+)$", name):
    # if matches:
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
