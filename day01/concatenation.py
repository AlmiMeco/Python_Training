


name = 'Almi'
age = 22

print('My name is ' + name)
# print("My age is" + age) -> error {TypeError: can only concatenate str (not "int") to str}

# In Python concatenation is done by 'placeholders' -> {}
print("My age is {}".format(age))
print(f'I am named {name} and I am {age} yrs old')
# print(f) -> allows you to format in an easier way
