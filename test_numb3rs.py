import pytest
from numb3rs import validate

def test_outOfRange():
    assert validate("98.456.34.1") == False

def test_negativeInteger():
    assert validate("87.96.123.-9") == False

def test_alphabetWithin():
    assert validate("74.23.try.hello") == False

def test_dotSuffix():
    assert validate("45.23.65.55.") == False

def test_normal():
    assert validate("78.36.98.123") == True
