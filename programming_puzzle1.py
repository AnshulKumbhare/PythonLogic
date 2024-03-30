"""
Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least
three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

# li = [19, 19, 15, 5, 3, 5, 5, 2]
# li = [19, 15, 15, 5, 3, 3, 5, 2]
li = [19, 19, 5, 5, 5, 5, 5]

if (li.count(19) == 2) and (li.count(5) >= 3):
    print(True)
else:
    print(False)
