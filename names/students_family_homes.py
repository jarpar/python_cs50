import csv

students = []

with open("students_family_homes.csv") as file:
    reader = csv.reader(file, delimiter=",", quotechar='"')
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
