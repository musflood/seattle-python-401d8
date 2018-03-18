# Class Inheritance and Composition

## Class Inheritance in Python
Any Object-Oriented language will enable the use of inheritance in some form or fashion, including Python. Classes can inherit from other classes, or even multiple classes. The class (perhaps think of the ancestor?) that's being inherited from is typically referred to as the superclass. The inverse, the class doing the inheriting, is typically referred to as the subclass.

Here's a quick syntax view of how code inheritance is structured in Python:
```python
class SubClass(SuperClass):
    pass
```
Note that the `SuperClass` is defined as a parameter on the class definition.

Lets take a look at a more practical example.
```python
class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def __str__(self):
        return '{} {}'.format(self.first, self.last)

    def Name(self):  # Let's note that we would normally define this functionality as a magic method on the class... as in __str__ above.
        return '{} {}'.format(self.first, self.last)


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        Person.__init__(self, first_name, last_name)
        self.eid = employee_id

    def GetEmployeeInfo(self):
        return '{} {}, #{}'.format(self.first, self.last, self.eid)


susan = Person('Susan', 'Malarky')
rachael = Employee('Rachael', 'Wagner', 1138)

susan.Name()
# 'Susan Malarky'
rachael.Name()
# 'Rachael Wagner'
susan.GetEmployeeInfo()
# ... AttributeError: 'Person' object has no attribute 'GetEmployeeInfo'...
rachael.GetEmployeeInfo()
# 'Rachael Wagner, #1138'
```

## Accessing Parent Methods - `super()`
Another way of specifically working with the SuperClass is through the use of the `super` keyword.
```python
class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def Name(self):
        return '{} {}'.format(self.first, self.last)


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(self, first_name, last_name)
        # The following line is Python 2, while the above line note including the super class is a Python 3 only syntax.
        # super(Person, self).__init__(self, first_name, last_name)
        self.eid = employee_id

    def GetEmployeeInfo(self):
        return '{} {}, #{}'.format(self.first, self.last, self.eid)


susan = Person('Susan', 'Malarky')
rachael = Employee('Rachael', 'Wagner', 1138)
```
