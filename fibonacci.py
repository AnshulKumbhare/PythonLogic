"""
write a python program to print fibonacci Series up to n numbers
"""

n = int(input("Enter n: "))

def fibonacci_series(num):
    a = 0
    b = 1
    print(a, b, end=" ")

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

fibonacci_series(n)