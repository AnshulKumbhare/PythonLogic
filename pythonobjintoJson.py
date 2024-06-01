"""
Write a Python program to convert Python object to JSON data.
"""

import json

python_obj = {
    "name": "Anshul",
    "age": 23,
    "dob": "2001-03-16",
}
print(type(python_obj))


json_obj = json.dumps(python_obj)
print(json_obj, type(json_obj))
