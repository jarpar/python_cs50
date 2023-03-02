with open("names.txt", "a") as file:
    for line in file:
        print("hello, ", line.rstrip())
