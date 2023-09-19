

s = 'Python'

for each in s:
    print(each)

print('--------------------------------')

# Looping from first index [0] to last [len()] *len() == .length() -1 in Java*
for i in range(0, len(s)):
    # print(i)
    print(s[i])

print('--------------------------------')

# Reverse Looping (reversed() function)
for i in reversed(range(0, len(s))):
    print(s[i])
