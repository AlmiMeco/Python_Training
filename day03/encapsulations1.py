"""
Similar to Java Python has encapsulation
Encapsulation is facilitated thru private fields and Getters/Setters
Two underscores (__) before a field/metod means Private access modifier
"""


class Person:

    def __init__(self, name: str, age: int):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)


    #     Getter w/ restrictions
    def get_name(self) -> str:

        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f"Invalid name : {self.__name}")

        return self.__name


    # Setter w/ restrictions
    def set_name(self, name):

        if type(name) != str:
            raise RuntimeError("Person name MUST be String")
        if name == '':
            raise RuntimeError("Person name CANNOT be empty")

        self.__name = name


    def get_age(self) -> int:

        return self.__age


    def set_age(self, age):

        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid Age: {age}')

        self.__age = age


person1 = Person('Almi', 22)

print(person1.get_name())
print(person1.get_age())
print(person1.__dict__)