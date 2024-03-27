"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
"""

f = input("Enter the file name: ")

l_file = f.split(".")
print(l_file[-1])