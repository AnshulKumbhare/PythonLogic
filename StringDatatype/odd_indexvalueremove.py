"""
Write a Python program to remove characters that have odd index values in a given string.
"""

s = input('Enter s: ')

res = ""

for i in range(len(s)):
    if i % 2 == 0:
        res += s[i]

print(res)