"""
Write a Python program to reverse a string.
"""
s = input("Enter s: ")

def reverse_string(s):
    rev_s = s[::-1]
    return rev_s

print(reverse_string(s))