import pytest


def add(a, b):
    """
    Function that accepts two integers as arguments and returns the sum total
    Arguments:
        (a, b) => Integer
    Returns => Integer
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError('Argument(s) invalid. Must be valid Int')
    return a + b


def test_add_two_valid_ints():
    assert add(1, 1) == 2


def test_string_args_should_error():
    """
    test that you cannot provide two strings as arguments
    should return error
    """
    with pytest.raises(TypeError) as err:
        add('a', 'b')

    with pytest.raises(TypeError) as err:
        add('a', 1)

    assert str(err.value) == 'Argument(s) invalid. Must be valid Int'
