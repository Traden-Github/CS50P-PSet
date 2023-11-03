import plates

def test_useless():
    assert plates.is_valid("FD,89") == False

def test_length():
    assert plates.is_valid("DFGH9860") == False

def test_firstTwoLetter():
    assert plates.is_valid("S3679") == False

def test_numberBetween():
    assert plates.is_valid("SD5T7") == False

def test_zeroPrefix():
    assert plates.is_valid("DG078") == False
