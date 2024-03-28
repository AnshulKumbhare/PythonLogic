"""
Write a Python program to calculate the body mass index.
BMI = weight(kgs) / height (metre square)
"""

w = float(input("Enter weight(in kgs): "))
h = float(input("Enter height (in metres): "))

bmi = w / h ** 2

print(bmi)