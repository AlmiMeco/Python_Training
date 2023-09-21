import json
import os

"""
Importing/Loading JSON file 
Json files are key=value (Dictionary/Map)
        json.load  = converts (json -> dict) 
        json.dumps = converts (dict -> json)
"""

path = "files/Test.json"

"""
Reading JSON file
"""

# Stored As String
json_file = open(path, 'r')

# Stored as dictionary
dictionary = json.load(json_file)

print(dictionary)

json_file.close()

"""
Writing to JSON file
"""

print('--------------------Converting students (dict) to JSON FILE-----------------------')

# Dictionary of Students
students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

# Creating New JSON file 'students_data.json'
json_file = open("files/students_data.json", 'w')

# Converting dictionary obj -> json object (indent=2 -> JSON formatting)
json_object = json.dumps(students, indent=2)

# Populating JSON FILE w/ json object (previously dictionary object)
json_file.write(json_object)

json_file.close()

