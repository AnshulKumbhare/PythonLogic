import json

json_data = '{"Name" : "David", "Class" : "I", "Age" : 6}'

python_obj = json.loads(json_data)
print(python_obj)

print(python_obj['Name'])
print(python_obj['Class'])
print(python_obj['Age'])