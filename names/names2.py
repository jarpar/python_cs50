name = input("What's oyur name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
