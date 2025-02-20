import pytest


def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacio(a,b):
    return a*b

def divisio(a,b):
    return a/b

def majuscules(text):
    return text.upper()

def minuscules(text):
    return text.lower()

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(10, 5) == 5
    assert resta(0, 0) == 0

def test_divisio():
    with pytest.raises(ZeroDivisionError):
        divisio(10, 0)
    assert divisio(2,2) == 1

def test_majuscules():
    assert majuscules('AbCdEfGh') == 'ABCDEFGH'

def test_minuscules():
    assert minuscules('AbCdEfGh') == 'abcdefgh'




