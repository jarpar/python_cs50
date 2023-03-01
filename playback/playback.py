"""
prompts the user for input
outputs that same input, replacing each space with ... (i.e., three periods).
"""

def main():
    get_input()


def get_input():
    print(str(input("Enter your sentence: ").replace(" ", "...")))


main()


