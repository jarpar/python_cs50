score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
elif score >= 50 and score < 60:
    print("Grade: E")
elif score >= 40 and score < 60:
    print("Grade: F")
elif score >= 30 and score < 40:
    print("Grade: G")
elif score >= 20 and score < 30:
    print("Grade: H")
elif score >= 10 and score < 20:
    print("Grade: I")
elif score >= 0 and score < 10:
    print("Grade: J")
else:
    print("Too low to get grade!")
