names = []

for _ in range(3):
    names.append(input("What's your name? "))

for n in sorted(names):
    print(f"hello, {n}")
