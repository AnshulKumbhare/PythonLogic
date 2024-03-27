"""
Write a Python program to create a histogram from a given list of integers
"""

list_histogram = [10, 2, 5, 4, 1, 6, 9]

n = len(list_histogram)
print("Histogram\n")
for i in list_histogram:
    for j in range(i):
        print("#", end="")
    print()