"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number(li):
    e_l = []
    for i in li:
        if i % 2 == 0:
            e_l.append(i)
    return e_l

print(even_number(l))