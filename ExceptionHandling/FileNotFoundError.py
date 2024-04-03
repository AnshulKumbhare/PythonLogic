"""
Write a Python program that opens a file and handles a
FileNotFoundError exception if the file does not exist.
"""

try:
    fp = open('contact.txt', 'r')
    fp.read()
    fp.close()
except FileNotFoundError:
    print("There is no file with the given name.")