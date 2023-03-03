students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        # v1:
        # students.append(f"{name} is in the {house}")

        # v2:
        # student = {}
        # student["name"] = name
        # student["house"] = house

        # v3 is the same as v2 but another notation:
        student = {"name": name, "house": house}
        students.append(student)

# for student in sorted(students):
# print(student)
for student in students:
    print(f"{student['name']} is in {student['house']}")
