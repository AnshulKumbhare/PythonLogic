"""Write a Python program to determine if a variable is defined or not"""

try:
    y
except NameError:
    print("Variable not defined")
else:
    print("variable defined")