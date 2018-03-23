from uuid import uuid4


class BasicClass:
    """
    Example class that unsuitable for instances
    This class does NOT take any arguments when used
    """
    basic_info = ['scott', True, 'blue', 35]


# BasicClass.basic_info = > ['scott', True, 'blue', 35]


class MyClass:
    def __init__(self, one, two):
        self.default = (1, 4)
        self.arg_one = one
        self.arg_two = two

    def __str__(self):
        return 'I am a magic method printing all the things about this class: {}: {}'.format(
            self.arg_one, self.arg_two)

    def __len__(self):
        return len(self.default)


myclass = MyClass([], {})
print(myclass.__len__())
print(len(myclass))


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def say_hello(self):
        return 'Hello, I am {}'.format(self.first)

    def __str__(self):
        return 'Hello my name is {} {}'.format(self.first, self.last)


# class SubClass(SuperClass):...
class Employee(Person):
    def __init__(self, first_name, last_name):
        # Python 3 syntax:
        super().__init__(first_name, last_name)
        # Python 2 syntax: super(Person, self).__init__(first_name, last_name)
        self.id = uuid4()

    def __monkey__(self):
        return 'I like bananas'

    def __repr__(self):
        return '<Employee ID: {}>'.format(str(self.id))
