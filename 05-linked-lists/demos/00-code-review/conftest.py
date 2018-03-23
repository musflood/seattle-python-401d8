import pytest
import classes as c


# @decorator
@pytest.fixture
def basic_class():
    return c.BasicClass


@pytest.fixture
def my_class():
    return c.MyClass('hello', 'world')


