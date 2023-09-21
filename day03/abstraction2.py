import numbers
from abc import ABC, abstractmethod

"""
abc: built-in Python module 
ABC: Abstract Class inside abc module
abstractmethod: annotation annotated on Abstract methods (makes the method MANDATORY to be implemented by subClass)
"""

# Abstract Class
class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> numbers:
        return self.width * self.length


class Cube(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


# -----------------------------------------------
square1 = Square(5)
print(square1)
# Square{'name': 'Square', 'side': 5}

print(square1.area())
# 25

