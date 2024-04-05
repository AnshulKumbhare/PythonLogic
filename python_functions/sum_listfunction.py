"""
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
"""

l = [8, 2, 3, 0, 7]

def sum_list(l):
    s = 0
    for i in l:
        s += i
    return s

print(sum_list(l))