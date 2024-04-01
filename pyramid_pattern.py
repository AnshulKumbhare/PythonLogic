"""
Write a Python program to construct the following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5):
    for j in range(i + 1):
        print("* ", end=" ")
    print()

for i in range(4):
    for j in range(4, i, -1):
        print("* ", end=" ")
    print()