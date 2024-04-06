"""Write a Python program to execute a string containing Python code."""

code = """
x = 10
y = 20
m = max(x, y)
print(f"{m} is larger")
"""

exec(code)
