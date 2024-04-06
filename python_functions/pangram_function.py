"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""
import string
s = input("Enter s: ")

def chk_pangram(s):
    s = s.lower()
    alpha = string.ascii_lowercase
    flag = True

    for i in alpha:
        if i not in s:
            flag = False
            break
    return flag

if chk_pangram(s):
    print("It is a Pangram")
else:
    print("It is not a Pangram")
