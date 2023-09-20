"""
Lists in Python
Created by placing MORE than one object in [] seperated by a comma
Any data type can be stored in a list
Values in a List CAN be updated (by index # [])
Lists support forward && reverse indexing
* Lists size is DYNAMIC *
"""

groceries = ['Eggs', 'Milk', 'Bread']

"""
Append -> adds ONE element to our list
"""
groceries.append('Chicken')
print(groceries)
# ['Eggs', 'Milk', 'Bread', 'Chicken']

"""
Extend -> adds MULTIPLE () elements to our list
"""
groceries.extend(("Beef", "Wine", 'Cereal'))
print(groceries)
# ['Eggs', 'Milk', 'Bread', 'Chicken', 'Beef', 'Wine', 'Cereal']

"""
Reversing a List (same as str (splicing) )
"""
reversed_groceries_list = groceries[::-1]
print(reversed_groceries_list)
# ['Cereal', 'Wine', 'Beef', 'Chicken', 'Bread', 'Milk', 'Eggs']

print('-----------------------------------------------')

"""
Updating elements of a List by RANGE
[x:x] = range of elements
[x:x] -> splicing 
"""
# Splicing
print(groceries[2:3])
# Range
groceries[2:3] = ['Cow', 'Bird']
print(groceries)
# ['Eggs', 'Milk', 'Cow', 'Bird', 'Chicken', 'Beef', 'Wine', 'Cereal']

print('-----------------------------------------------')

"""
Sorting a List 
In Ascending .sort()
In Descending .sort(reverse=True)
"""

nums = [10, 40, 430, 299, 2]

nums.sort()
print(nums)
# [2, 10, 40, 299, 430]

nums.sort(reverse=True)
print(nums)
# [430, 299, 40, 10, 2]

print('-----------------------------------------------')

"""
Converting one Data Structure to another 
Tuple --> List
Conversion is done using the Data Structure Constructor... ( list(), tuple(), set(), etc... )
"""

tuple_data_structure = 'Java', 'Python', 'C#', 'GoLang'
list_data_structure = list(tuple_data_structure)

print(tuple_data_structure)  # -> ('Java', 'Python', 'C#', 'GoLang')
print(list_data_structure)   # -> ['Java', 'Python', 'C#', 'GoLang']

print('----------------------Comprehensions-------------------------')

"""
List Comprehensions are used to create a new list based on condition
MUST return List or Set (no Tuple) 
"""

nums.clear()

for i in range(1, 51):
    nums.append(i)

print(nums)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
# 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

divisible_by_5 = [ x for x in nums if x % 5 == 0]
print(divisible_by_5)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print('-----------------------------------------------')

odd_nums = [x for x in nums if x % 2 != 0]
even_nums = [x for x in nums if x % 2 == 0]

print(odd_nums)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
print(even_nums)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
