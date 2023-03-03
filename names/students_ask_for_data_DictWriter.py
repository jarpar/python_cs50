import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students_ask_for_data_DictWriter.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
