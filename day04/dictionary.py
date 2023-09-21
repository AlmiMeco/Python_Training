"""
Dictionary in Python == Map in Java
• Created by placing all the pairs inside curly brackets {key : value} separated by commas
• Collection of pairs
• Data structure based on the key + value pairs
• Size is dynamic, and can be increased/decreased
• The Items in the dictionary are changeable
• Keys MUST be unique ; Values CAN be duplicates
• Items in the dictionary are ordered, changeable, and can be of *ANY* data type
• * Dictionary DOES NOT have index #s (no slicing) *
"""


dictionary = {'first_name': 'Almi', 'last_name': 'Meco', 'age': 22}

print(dictionary)
# {'first_name': 'Almi', 'last_name': 'Meco', 'age': 22}

# Updating a dictionary pair w/ update() method || by specifying [key]
dictionary['age'] = 32

print(dictionary)
# {'first_name': 'Almi', 'last_name': 'Meco', 'age': 32}

print('-------------------Iterating Over a Dictionary-------------------------')
# Iterating The Keys
for k in dictionary.keys():
    print(k)

# Iterating The Values
for k in dictionary.values():
    print(k)

print('------------------------------------------------------------------')

# Iterating both Keys & Values
for k in dictionary.keys():
    print(f'Key-> {k} : Value-> {dictionary[k]}')




