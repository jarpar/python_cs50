# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("---")

for s in students:
    print(s)

print("----")

for s in students:
    print(s, students[s], sep=", ")
