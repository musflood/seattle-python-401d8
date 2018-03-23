# Typically do not want this single instance so that we can avoid changing values and creating interdependant tests
import classes as c
import pytest
# person = c.Person('Code', 'Fellow')


def test_basic_class(basic_class):
    assert basic_class.basic_info[0] == 'scott'


def test_basic_class_length(basic_class):
    assert len(basic_class.basic_info) == 4


def test_my_class_instance_arg_one(my_class):
    assert my_class.arg_one == 'hello'


def test_my_class_instance_arg_two(my_class):
    assert my_class.arg_two == 'world'


# def test_person_class():
#     assert person.first == 'Code'


# You can create fixtures directly in the test file as well
@pytest.fixture
def person_class():
    return c.Person('Code', 'Fellow')


def test_person_class(person_class):
    assert person_class.first == 'Code'
    person_class.first = 'WAT'
    assert person_class.first == 'WAT'


def test_person_class_first(person_class):
    assert person_class.first == 'Code'

