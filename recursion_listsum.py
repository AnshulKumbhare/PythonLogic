"""
Write a Python program to calculate the sum of a list of numbers using recursion.
"""
l = [5, 10, 50, 35]

# method 1
length = len(l)
n = 0
def recur_listsum(l, length, n):
    if l.index(l[n]) == length - 1:
        return l[n]
    else:
        return l[n] + recur_listsum(l, length, n + 1)

print(recur_listsum(l, length, n))

# method 2

def recur_listsum2(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recur_listsum2(l[1:])

print(recur_listsum2(l))