import guessing_game as gg
import pytest as pt


def test_print_welcome():
    msg = gg.print_welcome()
    assert type(msg) is str
    assert 'Welcome' in msg
    # assert gg.GAME_OPTIONS['username] in msg


# Do not test user input... you don't need to worry about it.


def test_check_user_input_valid_int():
    assert gg.check_user_input(25, 25) is True
    assert gg.check_user_input(2, 1) is False


def test_check_user_input_invalid():
    with pt.raises(TypeError) as err:
        gg.check_user_input('a', 25)

    assert str(err.value) == 'Guess must be Integer'

