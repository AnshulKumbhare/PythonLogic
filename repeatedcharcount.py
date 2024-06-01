"""
Write a Python program to count repeated characters in a string.
"""

s = "thequickbrownfoxjumpsoverthelazydog"
d = {}
for c in s:
    if s.count(c) > 1 and c not in d:
        d.update(((c, s.count(c)),))

print(d)