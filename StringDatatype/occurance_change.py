"""
 Write a Python program to get a string from a given string where all occurrences
 of its first char have been changed to '$', except the first char itself.
"""

s = input('Enter a string: ')

char = s[0]

new_s = char + s[1::].replace(char, "$")
print(new_s)