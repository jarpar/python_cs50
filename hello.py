# Ask user for their name
name = input("What's your name? ").strip().title()
# Say hello to user
print("hello,", name, sep=" ")
print('hello, "friend"')
print(f"hello, {name}")
# remove whitespace from string
name = name.strip()
print(f"hello, {name}")

# capitalize user's name
name = name.title()
print(f"hello, {name}")
print("Good bye!")
