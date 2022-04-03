#Testing file

#Importing all functions from example.py for testing purposes
from example import add
from example import substract
from example import multiply
from example import onpow
from example import modulus

def test_add():
    assert add(5, 6) == 11

def test_substract():
    assert substract(10, 3) == 7

def test_multiply():
    assert multiply(5, 6) == 30

def test_onpow():
    assert onpow(2, 2) == 4

def test_modulus():
    assert modulus(10, 3) == 1
