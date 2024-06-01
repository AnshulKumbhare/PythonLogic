import json
python_dict = {"name": "David", "age": 6, "class":"I"}
python_list = ["Red", "Green", "Black"]
python_str = "Python Json"
python_int = 1234
python_float = 21.34
python_T = True
python_F = False
python_N = None

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_list)
json_int = json.dumps(python_int)
json_float = json.dumps(python_float)
json_T = json.dumps(python_T)
json_F = json.dumps(python_F)
json_N = json.dumps(python_N)

print("json dict : ", json_dict)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_int)
print("json number2 : ", json_float)
print("json true : ", json_T)
print("json false : ", json_F)
print("json null ; ", json_N)