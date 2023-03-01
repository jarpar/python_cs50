def main():
    print_square1(3)
    print("----")
    print_square(3, 4)
    print("----")
    print_square(4, 3)

def print_square(height, width):
    for h in range(height):
        for w in range(width):
            print("#",end="")
        print("")

def print_square1(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


main()
