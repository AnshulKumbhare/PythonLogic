"""
fibonacci with recursion
"""

n = int(input("Enter n: "))

a = 0
b = 1
print(a, b, end=" ")
n = n - 2
def fibonacci_recur(a, b, n):
    if n == 1:
        c = a + b
        return c
    else:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        return fibonacci_recur(a, b, n - 1)

print(fibonacci_recur(a, b, n))