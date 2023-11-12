from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    cookies = Jar()
    with pytest.raises(ValueError):
        assert cookies.deposit(13)


def test_withdraw():
    cookies = Jar()
    cookies.deposit(5)
    with pytest.raises(ValueError):
        cookies.withdraw(6)
