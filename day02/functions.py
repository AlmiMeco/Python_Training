

"""
Functions in Python are like methods in Java
They are specified by the 'def' keyword
"""
import numbers


def add(num1, num2):
    return num1 + num2


print(add(10,2))
# -> 12


def multiply(num1: numbers, num2: numbers) -> numbers:
    return num1 * num2


print(multiply(10,2))
# -> 20
