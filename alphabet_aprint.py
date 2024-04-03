"""
Write a Python program to print the alphabet pattern 'A'.
Expected Output:

  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   *
"""


for i in range(7):
    if i == 0:
        print(" *** ")
    elif i == 3:
        print("*****")
    else:
        print("*   *")
