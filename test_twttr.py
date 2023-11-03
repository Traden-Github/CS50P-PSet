from twttr import shorten

def test_a():
    assert shorten("gasclass") == "gsclss"

def test_e():
    assert shorten("ew, they peed everywhere") == "w, thy pd vrywhr"

def test_i():
    assert shorten("hi, I'm Kiwi") == "h, 'm Kw"

def test_o():
    assert shorten("oops, wrong poop") == "ps, wrng pp"

def test_u():
    assert shorten("u r guy") == " r gy"

def test_combo():
    assert shorten("Hi I'm Aubrey, I love you") == "H 'm bry,  lv y"

def test_numbers():
    assert shorten("1564645646468") == "1564645646468"

