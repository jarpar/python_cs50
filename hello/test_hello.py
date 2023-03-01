from hello import hello

def test_default():
    assert hello("world") == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
    
    assert hello("Jarek") == "hello, Jarek"

 