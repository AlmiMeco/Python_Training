"""
In Python classes are created ONLY for creating (instantiating) objects
"""
import numbers


class Employee:
    """
    __init__() in Python == constructor() in Java
    -> self == this
    * IN PYTHON THE CONST (__init__) IS ALSO RESPONSIBLE FOR INITIALIZING FIELDS *
    To override the const we just need to set default values to our Fields

    -> NO OVERRIDING IS NECESSARY IN PYTHON, one constructor (__init__) acts as ALL_ARGS && NO_ARGS && everything in b/w
    """

    def __init__(self, name: str = 'Default', job_title: str = 'Unemployed', salary: numbers = 0, age: int = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.age = age

    def work(self):
        print(f'{self.name} is working')

    # toString() method for Python
    def __str__(self):
        return f'{self.__dict__}'


# All Args
employee1 = Employee('Almi', 'Dev', 80000, 22)

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)
print(employee1.age)

print('------------------------------')

# One Arg
employee2 = Employee('Zander')
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)
print(employee2.age)

print('------------------------------')

# No Args
employee3 = Employee()
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)
print(employee3.age)

print('------------------------------')

# Calling Methods (func)
employee1.work()
employee2.work()
employee3.work()

print('------------------------------')

# Calling __str__ (toString()) function
print(employee1)
print(employee2)
print(employee3)
