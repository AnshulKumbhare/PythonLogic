"""
We are making n stone piles! The first pile has n stones.
If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones.
Each pile must more stones than the previous pile but as few as possible.
Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""


n = int(input("Enter n: "))
li = list()
s = n
if n % 2 == 0:
    li.append(n)
    for i in range(1, n):
        s += 2
        li.append(s)
else:
    li.append(n)
    for i in range(1, n):
        s += 2
        li.append(s)

print(li)