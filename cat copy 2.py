def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        number = int(input("What's the number of cats? "))
        if number >= 0:
            break
    return number


def meow(n):
    for _ in range(n):
        print("meow\n", end="")


main()
