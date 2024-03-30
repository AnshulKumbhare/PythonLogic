"""
Write a Python program that accepts a list of integers and calculates the length and the fifth element.
Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
"""

l = []
n = int(input("Enter number of values you need to enter: "))

for i in range(n):
    val = int(input(f"Enter value {i + 1}: "))
    l.append(val)

length = len(l)
fifth_ele = l[4]

def chk_condition(l, length, fifth_ele):
    if (length == 8) and (l.count(fifth_ele) == 3):
        return True
    else:
        return False

print(chk_condition(l, length, fifth_ele))