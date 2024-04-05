"""
Write a  Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
"""
l = [8, 2, 3, -1, 7]

def mul_list(l):
    m = 1
    for i in l:
        m *= i
    return m

print(mul_list(l))