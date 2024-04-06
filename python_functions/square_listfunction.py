"""
Write a Python function to create and print a list where the values are the squares of numbers between
1 and 30 (both included).
"""

def square_list():
    l = []
    for i in range(1, 31):
        sqr = i ** 2
        l.append(sqr)

    return l

print(square_list())