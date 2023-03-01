"""
prompts the user for a str
outputs that same text but with all vowels (A, E, I, O, and U) omitted
"""


def main():
    tweet = input("What to tweet? ")
    get_tweet(tweet)
    # get_tweet("PYTHON python PYTHON python python PYTHON")


def get_tweet(sentence_in):
    vowels = ["a", "e", "i", "o", "u"]
    for s in sentence_in:
        s_lowercased = str(s).lower()
        is_vowel = False
        for v in vowels:
            if s_lowercased == v:
                is_vowel = True
        if is_vowel == False:
            print(f"{s}", end="")
            is_vowel = False

    print()


if __name__ == "__main__":
    main()
