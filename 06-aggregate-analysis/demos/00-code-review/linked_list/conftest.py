import pytest
from linked_list.linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def predefined_ll():
    return LL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
