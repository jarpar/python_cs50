"""
convert that accepts a str
returns :) :( converted /slightly-smiling-face//slightly-frowning-face/
other text unchanged

"""


def main():
    sentence = str(input("Enter the sentence: "))
    sentence = convert(sentence)
    print(sentence)


def convert(sentence):
    return str(
        sentence.replace(":)", "\N{slightly smiling face}").replace(
            ":(", "\N{slightly frowning face}"
        )
    )


main()
