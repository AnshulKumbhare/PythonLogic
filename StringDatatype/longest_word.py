"""
Write a Python function that takes a list of words and return the longest word and the length of the
longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

l = []
n = int(input("Enter number of words you need to Enter: "))

for i in range(n):
    word = input("Enter word: ")
    l.append(word)

longest_word = ""
longest_word_length = 0
for i in l:
    if len(i) > len(longest_word):
        longest_word = i
        longest_word_length = len(i)

print(f"Longest word {longest_word}, \nLongest word length {longest_word_length}")