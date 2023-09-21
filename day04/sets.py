"""
Sets -> Similar to sets in Java
• Size is dynamic, and can be increased/decreased
• The elements in the set are unchangeable
• Set does NOT accept duplicated elements
• Elements in the set do NOT have index numbers -> That means NO slicing
• Created by placing all the elements inside curly brackets {} separated by commas
"""

set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}


print('-----------------------difference---------------------------')
# difference(): compares two sets and returns a new set which contains the items that only exist in first set

print(set1.difference(set2))
# {2, 4}

print('-----------------------intersection---------------------------')
# intersection(): compares two sets and returns a new set which contains the common elements of two sets

print(set1.intersection(set2))
# {1, 3, 5}

print('-----------------------different_update---------------------------')
# different_update(): removes the elements of the first Set that exist in the second Set

different_update_set = set1.difference_update(set2)
print(different_update_set)

