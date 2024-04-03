"""
Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number
is an even number. The numbers obtained should be printed in a comma-separated sequence.
"""

# Method 1
for i in range(100, 401, 2):
    flag = True
    n = i
    while n > 0:
        r = n % 10
        if r % 2 != 0:
            flag = False
            break
        n = n // 10
    if flag:
        print(i)

print()
# Method 2

for i in range(100, 401, 2):
    l = list(str(i))
    if (int(l[0]) % 2 == 0) and (int(l[1]) % 2 == 0) and (int(l[2]) % 2 == 0):
        print(i)