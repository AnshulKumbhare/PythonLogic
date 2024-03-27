"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = 5
s = 0
for i in range(1, 4):
    s = s + n
    n = n * 10 + 5

print(s)