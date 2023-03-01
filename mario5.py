def main():
    print_square(3, 3)
    print("----")
    print_square(3, 4)
    print("----")
    print_square(4, 3)


def print_square(height, width):
    for h in range(height):
        for w in range(width):
            print("#",end="")
        print("")

main()
