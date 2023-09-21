from day03.abstraction2 import Shape, Square, Rectangle

"""
Polymorphism -> The ability for one obj (Shape) to take many forms (Square, Rectangle) 
"""

shape1: Shape = Square(5)

shape2: Shape = Rectangle(2, 5)


def display_area(shape: Shape):
    print(f'The {shape.name}\'s area is {shape.area()} ')


display_area(shape1)
display_area(shape2)
