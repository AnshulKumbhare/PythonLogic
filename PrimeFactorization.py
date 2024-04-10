"""
Prime Factorization
"""

n = int(input('Enter n : '))

def prime_factors(n):
    for i in range(2, n):
        if is_prime(i):
            x = i
            while n % x == 0:
                print(f"{i}", end=" ")
                x = x * i

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_factors(n)