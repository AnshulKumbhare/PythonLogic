"""
Write a Python program to convert height (in feet and inches) to centimeters.
"""

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

inches += feet * 12

cm = inches * 2.54

print(f"{cm} cm")