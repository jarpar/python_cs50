import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students_ask_for_data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
