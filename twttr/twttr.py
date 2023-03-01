"""
prompts the user for a str
outputs that same text but with all vowels (A, E, I, O, and U) omitted
"""


def main():
    tweet = input("What to tweet? ")
    get_tweet(tweet)


def get_tweet(sentence_in):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for s in sentence_in:
        is_vowel = False
        for v in vowels:
            if s == v:
                is_vowel = True
        if is_vowel == False:
            print(f"{s}", end="")
            is_vowel = False

    print()


if __name__ == "__main__":
    main()
