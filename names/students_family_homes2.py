import csv
# remember add to csv file dictionary keys (ex: name, home)

students = []

with open("students_family_homes2.csv") as file:
    reader = csv.DictReader(file, delimiter=",", quotechar='"')
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
