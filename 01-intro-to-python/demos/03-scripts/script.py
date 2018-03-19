

def foo():
    print('I am not in the conditional')


if __name__ == '__main__':
    foo()

    answer = 4

    while True:
        user_input = int(input('Give me a number between 1-10\n>\t'))
        if user_input == answer:
            print('good job - you got it')
            break

