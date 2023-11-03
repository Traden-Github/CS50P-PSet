from bank import value

def test_hello():
    assert value("Hello, Birch") == 0

def test_h():
    assert value("Hey, Birch") == 20

def test_none():
    assert value("Birch") == 100

def test_number():
    assert value("486") == 100
