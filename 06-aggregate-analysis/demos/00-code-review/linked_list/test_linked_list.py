import pytest
from linked_list.linked_list import LinkedList as LL


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_find_an_int_in_ll(predefined_ll):
    assert predefined_ll.find(1) is True
    assert predefined_ll.find(11) is False


def test_noniterable_as_argument():
    with pytest.raises(TypeError):
        LL(1234)
