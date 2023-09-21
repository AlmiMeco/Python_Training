import json
import csv
import os

"""
• The build-in method open() is used for file handlings. Returns file object (BefferReader from Java)
• The method takes two arguments: open( file_path , mode)
• File handling is decided based on the second argument (mode) that’s passed to the method
    MODES :
        “r” ->  Read. Used to open a file for reading.     (Gives Error if the file does not exist)
        “w” ->  Write. Used to open a file for Writing.    (Creates the file if the file does not exist)
        “a” ->  Append. Used to open a file for appending. (Creates the file if the file does not exist)
        “x" ->  Create. Used to create a file.             (Given error if the file was already created)
"""

path = "C:/Users/Almi's PC/Desktop/my_file.txt"

# Reading A File ('r')
text_file = open(path, 'r')
print(text_file.read())
text_file.close()

print('----------------------------------------')

path2 = 'files/new_file.txt'

# Writing A File ('w') *creates file if non-exisitng*
text_file2 = open(path2, 'w')
text_file2.write('This is a new file created by the open() method in Python')
text_file2.close()

print('----------------------------------------')
# Removing A file

# os.remove(path2)


