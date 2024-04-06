"""
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a
hyphen-separated sequence after sorting them alphabetically.
"""

s = input("Enter s: ")

def sort_aphabetically(words):
    l = words.split("-")
    l.sort()
    print("-".join(l))

sort_aphabetically(s)