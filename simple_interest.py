"""
Write a Python program to compute the future value of a specified
principal amount, rate of interest, and number of years.
"""

amt = int(input("Enter amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
t = int(input("Enter time(in years): "))

si = (amt * rate_of_interest * t) / 100
print(si)
