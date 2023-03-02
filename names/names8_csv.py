names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")

print("----\nList reverse sorted:\n----")

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
