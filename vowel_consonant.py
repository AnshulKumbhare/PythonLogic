"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

letter = input("Enter letter: ")

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if letter in vowel:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")