class Person:

    def __init__(self, name: str = 'Blank Name', age: int = 0):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age

    # Getter in Python Syntax
    @property
    def person_name(self):

        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f"Invalid name : {self.__name}")

        return self.__name

    # Setter in Python Syntax
    @person_name.setter
    def person_name(self, name):

        if type(name) != str:
            raise RuntimeError("Person name MUST be String")
        if name == '':
            raise RuntimeError("Person name CANNOT be empty")

        self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age):

        if type(age) != int:
            raise RuntimeError(f'Age given: \'{age}\' is not an Integer')

        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid Age: {age}')

        self.__age = age


person1 = Person()
person1.person_name = 'Almi'
person1.person_age = 22

print(person1.person_name)
print(person1.person_age)



