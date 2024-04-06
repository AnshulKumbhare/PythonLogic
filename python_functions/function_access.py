"""
Write a Python program to access a function inside a function.
"""

def chk_prime(n):
    flag = True
    if n == 1:
        flag = False
    elif (n == 2 or n == 3):
        flag = True
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
    return flag

def main():
    n = int(input("Enter number: "))
    f = chk_prime(n)
    if f:
        print("is Prime")
    else:
        print("Not prime")

main()