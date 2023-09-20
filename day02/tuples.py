"""
Tuples in Python are like Array in Java
Tuples MUST include MORE than one element seperated by a *comma*
Tuples *can* (not required) be encapsulated by parenthesis
Tuples *can* include ANY data type
* Tuples size is FIXED *
"""

days = 'M', 'T', 'W', 'TH', 'F', 'S', 'SU'
random_elements = 'Cow', 7, True, 'Hello World', 60

print(days[2])
# -> 'W'

print(len(days))
# -> 7

print('--------------------------------------')

""" Splicing a Tuple """

working_days = days[:5]
weekend = days[5:]

print(days)
# ('M', 'T', 'W', 'TH', 'F', 'S', 'SU')
print(working_days)
# ('M', 'T', 'W', 'TH', 'F')
print(weekend)
# ('S', 'SU')
print(random_elements)
# ('Cow', 7, True, 'Hello World', 60)

print('--------------------------------------')

""" Merging Tuples """

tuple1 = 1, 2, 3, 4
tuple2 = 5, 6, 7, 8

tuple3 = tuple1 + tuple2
print(tuple3)
# (1, 2, 3, 4, 5, 6, 7, 8)

""" Reversing a Tuple """

reversed_tuple = tuple(reversed(tuple3))
print(reversed_tuple)
# (8, 7, 6, 5, 4, 3, 2, 1)


""" Tuple Methods 
 index(): returns the forward index number of a specified element from the tuple
 count(): returns the frequency of a specified element from the tuple
"""
print(days.index('W'))
# -> 2
print(days.count('W'))
# -> 1

print('--------------------------------------')

""" Multi-Dimensional Tuples
- works the same as Multi-Dimensional Arrays in Java
"""

nested_tuple = ((1, 2, 3), (8, 9, 10), (50, 100))
print(len(nested_tuple))
# -> 3

print(nested_tuple[0])
# (1, 2, 3)
print(nested_tuple[1])
# (8, 9, 10)

print(nested_tuple[2])
# (50, 100)

print(nested_tuple[2][1])
# 100

