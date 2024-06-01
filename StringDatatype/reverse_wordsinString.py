"""
Write a Python program to reverse words in a string.
"""
import functools

s = "Hello This is Anshul Sandeep Kumbhare"
new_s = ""

new_l = list(map(lambda word: word[::-1], s.split(" ")))
print(new_l)

new_s += functools.reduce(lambda word1, word2: word1 + " " + word2, new_l)
print(new_s)