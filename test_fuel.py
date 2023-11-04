import pytest
from fuel import gauge, convert

def test_division0():
    with pytest.raises(ZeroDivisionError):
        assert gauge(convert("7/0"))

def test_over100():
    with pytest.raises(ValueError):
        assert gauge(convert("127/1"))

def test_below0():
    assert gauge(convert("-20/46")) == "E"

def test_notNumber():
    with pytest.raises(ValueError):
        assert gauge(convert("Cat/Dog"))

def test_fakeFracion():
    with pytest.raises(ValueError):
        assert gauge(convert("7/4"))

def test_Full():
    assert gauge(convert("99/100")) == "F"

def test_Empty():
    assert gauge(convert("1/101")) == "E"

def test_Mid():
    assert gauge(convert("3/4")) == "75%"

