def meow(n: int) -> str:
    """ "
    comment
    param n: bla bla bla

    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
