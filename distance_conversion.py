"""
Write a  Python program to convert the distance (in feet) to inches, yards, and miles.
"""

d_feet = int(input("Enter distance in feet: "))

inches = d_feet * 12
yard = d_feet * 0.3333
miles = d_feet * 0.000189394
print(inches, yard, miles)