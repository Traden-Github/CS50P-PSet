import pytest
from um import count

def test_suffix():
    assert count("Hi, um, I'm gay, um") == 2

def test_prefix():
    assert count("Um, um, um, yes") == 3

def test_wordsWithUM():
    assert count("Umbrella is the like the chum in mum") == 0

def test_combo():
    assert count("Um, I'm, um, summing up the fumbles I had in bum, um..., rum") == 3
