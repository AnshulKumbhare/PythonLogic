"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0) using recursion .
Test Data:
sum_series(6) -> 12  => 6 + (6 - 2) + (6 - 4)
sum_series(10) -> 30
"""

n = int(input("Enter n: "))

# Method 1
def recur_add(n, x = 0):
    if (n - x) == 0:
        return 0
    else:
        s = n - x
        return s + recur_add(n, x + 2)

print(recur_add(n))

# Method 2

def recur_add2(n):
    if n < 1:
        return 0
    else:
        return n + recur_add2(n - 2)

print(recur_add2(n))