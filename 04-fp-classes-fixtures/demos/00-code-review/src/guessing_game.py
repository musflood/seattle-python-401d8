from random import randint


def print_welcome():
    """Doc Strings are gud"""
    return """
    ** Welcome to my guessing game.
    ** Guess a number between 1-100.
    ** Type 'quit' to exit.
    """


def get_user_input():
    """Doc Strings are gud"""
    return input('Guess a number\n')


def check_user_input(guess, answer):
    """Doc Strings are gud"""
    if guess == 'quit':
        exit_program()

    return int(guess) == answer


def generate_answer():
    """Doc Strings are gud"""
    return randint(1, 100)


def exit_program():
    """Doc Strings are gud"""
    exit(0)


def response(output):
    """Doc Strings are gud"""
    if output is True:
        return '''
            Congrats: you guessed it.
        '''
    return 'Try again...'


def main():
    """
    This will be the main function which acts as an entry point to the application
    when run as a script
    """
    print(print_welcome())
    # import pdb; pdb.set_trace()
    while True:
        user_input = get_user_input()

        try:
            output = check_user_input(user_input, GAME_OPTIONS['answer'])
            if output is True:
                print(response(output))
                break

        except ValueError:
            print(response(False))

        except ReferenceError:
            print(response(False))


GAME_OPTIONS = {
    'answer': generate_answer(),
    'number_of_guesses': 10,
    'username': 'THX1138',
    'hints': False,
    # ...
}

if __name__ == '__main__':
    print('answer is: ', GAME_OPTIONS['answer'])
    try:
        main()
    except KeyboardInterrupt:
        print('Thanks for playing... you quitter.')
