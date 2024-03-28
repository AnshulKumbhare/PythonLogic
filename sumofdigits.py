"""
Write a  Python program to calculate sum of digits of a number.
"""

n = int(input("Enter number: "))

s = 0
while n > 0:
    r = n % 10
    s += r
    n = n // 10

print(f"sum of digits of {n} is {s}")