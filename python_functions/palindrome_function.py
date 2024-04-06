"""
Write a Python function that checks whether a passed string is a palindrome or not.
"""

s = input("Enter a word: ")

def chk_palindrome(word):
    rev_word = word[::-1]
    if rev_word == word:
        return True
    else:
        return False

if chk_palindrome(s):
    print(f"{s} is a Palindrome.")
else:
    print(f"{s} is not a Palindrome.")