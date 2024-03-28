"""
Write a Python program to check whether a file exists.
"""

import os

print(os.path.isfile('main.py'))

print(os.path.isfile('doesnotexist.py'))