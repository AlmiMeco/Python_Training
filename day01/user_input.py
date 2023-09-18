
# input() -> Is the same as scanner from Java

name = input('Enter Your Name\n')

# print(f'My Name Is: {name}')
print('My name is: ' + name)

# print( help(input) ) <- the help() method gives documentation on given method

# -------------------------------------------------------------

score = int(input('What Was Your Score?\n'))

if 0<= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else: print('F')
else:
    print("Incorrect Grade Range")