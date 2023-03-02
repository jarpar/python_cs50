with open("students.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
