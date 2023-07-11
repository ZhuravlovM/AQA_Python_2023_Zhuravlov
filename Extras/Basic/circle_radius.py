# Write a Python program that calculates the area of a circle based on the radius entered by the user.

from math import pi

r = float(input("Input circle radius: "))
print("Radius of entered circle is: ", r)
print("Area of the circle is: " + str(pi * r**2))
