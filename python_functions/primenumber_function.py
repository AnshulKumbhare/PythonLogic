"""
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
"""

n = int(input("Enter n: "))

def chk_prime(num):
    flag = True
    if num == 1:
        flag = False
    elif (num == 2) or (num == 3):
        flag = True
    else:
        for i in range(2, n):
            if num % i == 0:
                flag = False
                break
    return flag

if chk_prime(n):
    print(f"{n} is Prime Number.")
else:
    print(f"{n} is not Prime Number. ")