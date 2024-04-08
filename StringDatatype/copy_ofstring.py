"""
Write a Python function to get a string made of 4 copies of the last two characters of a specified string
(length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
"""

def insert_end(s):
    return (s[-2] + s[-1]) * 4

print(insert_end("Python"))