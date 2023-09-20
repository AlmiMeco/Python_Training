"""
IN Python, we DO NOT have an 'Abstract' keyword
For that reason we do NOT call them 'Abstract Classes', instead we call them 'Base Classes'
"""
import numbers


# Base Class
class Shape:

    def __init__(self):
        self.name = type(self).__name__

    # Abstract Method (method w/out body)
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

# --------------------------------------------------------------------------------------------------------------------


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    # Abstracted Method
    def area(self) -> numbers:
        super().area()


square = Square(5)
print(square)
print(square.area())




