a = int(input("Enter a: "))
p = int(input("Enter power: "))

def power(a, p):
    if p == 1:
        return a
    else:
        return a * power(a, p - 1)

print(pow(a, p))