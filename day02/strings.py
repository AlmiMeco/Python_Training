

string = 'Python'

"""
String Indexing in Python has TWO different ways of indexing...
Forward Indexing: starts from 0 (first char) and increases by +1 for each char to the right {Standard Indexing like Java}
Reverse Indexing: starts from -1 (last char) and decreases by -1 for each char to the left 
"""
#Forward Indexing

print(string[0])
# -> 'P'
print(string[5])
# -> 'n'

# Reverse Indexing

print(string[-1])
# -> 'n'
print(string[-6])
# -> 'P'

print('------------------------------------------------------------------w')

"""
Slicing Strings (subStrings) [start:end]
By not giving beginning index  [:end]   -> slicing begins at index 0 
By not giving the ending index [start:] -> slicing stops at the last index
"""
subString1 = string[2:5]
subString2 = string[:3]
subString3 = string[3:]

print(subString1)
# -> 'tho'

print(subString2)
# -> 'Pyt'

print(subString3)
# -> 'hon'

"""
Printing the length of a String
len() method
"""
print(len(string))

print('------------------------------------------------------------------w')

"""
Reversing A String (or List or Tuple)
"""

reversed_list_by_method = str(reversed(string))
print(reversed_list_by_method)

reversed_list_by_splicing = string[::-1]
print(reversed_list_by_splicing)


