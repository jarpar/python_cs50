from tkinter import END


def main():
    score = int(input("Score: "))
    grade(score)
    if score == 0:
        exit()
    else:
        main()


def grade(score):
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    elif 50 <= score < 60:
        print("Grade: E")
    elif 40 <= score < 60:
        print("Grade: F")
    elif 30 <= score < 40:
        print("Grade: G")
    elif 20 <= score < 30:
        print("Grade: H")
    elif 10 <= score < 20:
        print("Grade: I")
    elif 0 <= score < 10:
        print("Grade: J")
    else:
        print("Too low to get grade!")


main()
