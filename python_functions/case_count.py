"""
Write a Python function that accepts a string and counts the number of upper and lower case letters.

"""

n = input("Enter a sentence: ")

def count_case(s):
    u_case = 0
    l_case = 0
    for i in s:
        if i.isupper():
            u_case += 1
        elif i.islower():
            l_case += 1
        else:
            continue

    return u_case, l_case

uppercase, lowercase = count_case(n)
print(f"uppercase letters: {uppercase}, lowercase letters: {lowercase}")
