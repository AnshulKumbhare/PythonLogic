"""
Write a Python program to strip a set of characters from a string.
"""

s = "The quick brown fox"
strip = "aeiou"

new_s = "".join(c for c in s if c not in strip)

print(new_s)

