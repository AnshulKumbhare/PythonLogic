"""
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
"""

c = float(input("Enter temperature in celsius: "))
f = float(input("Enter temperature in fahrenheit: "))

fah_temp = (c * 9 / 5) + 32
print(f"temp in fahrenheit is {fah_temp}")

cel_temp = (f - 32) * 5 / 9
print(f"temp in celsius is {cel_temp}")