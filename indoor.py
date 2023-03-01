"""
prompt input
output lowercase
punctuation whitespace unchanged
"""


def main():
    get_word()


def get_word():
    print(str(input("What words are you want to change? ")).lower())


if __name__ == "__main__":
    main()
