try:
    n = int(input("Enter Numerator: "))
    d = int(input("Enter denominator: "))

    ans = n / d
    print(ans)
except ZeroDivisionError:
    print("Number cannot be divided by zero.")
