"""
Write a Python program that takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column
of the array should be i*j.
"""

m = int(input("Enter m: "))
n = int(input("Enter n: "))

l = []
for i in range(m):
    l_inner = []
    for j in range(n):
        e = i * j
        l_inner.append(e)
    l.append(l_inner)

print(l)