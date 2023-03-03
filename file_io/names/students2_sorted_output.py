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


def get_name(student_name):
    return student_name["name"]


def get_house(student_house):
    return student_house["house"]


# for student in sorted(students):
# print(student)

print("Sorted by name in alphabetical order:")

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print("----")
print("Sorted by house in non-alphabetical order:")

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
