"""
Write a Python program to calculate the sum of harmonic series upto n terms.
Note: The harmonic sum is the sum of reciprocals of the positive integers.
"""

n = int(input("Enter n: "))
c = 1
def harmonicseries_recursion(n, c):
    if c == n:
        return 1 / n
    else:
        return (1 / c) + harmonicseries_recursion(n, c + 1)

print(harmonicseries_recursion(n, c))