"""
 Write a Python function that takes a sequence of numbers and determines whether all
 the numbers are different from each other.
"""


num = [12, 5, 98, 6, 4, 3, 2, 1, 99]

# Method 1
def chksequence_unique(num):
    flag = True
    for i in num:
        if num.count(i) != 1:
            flag = False
            break
    return flag

print(chksequence_unique(num))

# Method 2
def chksequence_unique2(num):
    if len(num) == len(set(num)):
        return True
    else:
        return False

print(chksequence_unique2(num))