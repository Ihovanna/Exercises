from pyparsing import one_of
from main import *
import pytest

def test_adds_num1_num2():
    #arrange
    n1 = 2
    n2 = 3

    #act
    result = addition(n1,n2)

    #assert
    assert result == 5


def test_adds_positive_and_negative_numbers():
    n1 = 20
    n2 = -5

    result = addition(n1,n2)

    assert result == 15


def test_argument_is_string():
    with pytest.raises(TypeError):
        addition("blue", 1)


def test_argument_is_True_boolean():
    n1 = True
    n2 = 1

    result = addition(n1,n2)

    assert result == 2


def test_argument_is_False_boolean():
    n1 = False
    n2 = 3

    result = addition(n1, n2)

    assert result == 3