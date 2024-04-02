"""
Write a Python program to get the Fibonacci series between 0 and 50.
"""

a = 0
b = 1
print(a, b, end=" ")

for i in range(2, 50):
    c = a + b
    if c >= 50:
        break
    print(c, end=" ")
    a = b
    b = c

