students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "name3", "house": "Gryffindor", "patronus": "patronus3"},
    {"name": "name4", "house": "Gryffindor", "patronus": "patronus4"},
    {"name": "name5", "house": "Gryffindor", "patronus": "patronus5"},
    {"name": "name5", "house": "Gryffindor", "patronus": "patronus5"},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
