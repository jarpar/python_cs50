name = input("What's oyur name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
