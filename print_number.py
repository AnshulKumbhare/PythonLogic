"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""

for i in range(7):
    if i in [3, 6]:
        continue
    print(i)