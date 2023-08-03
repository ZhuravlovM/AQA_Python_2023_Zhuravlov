# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        area = math.pi * self.radius ** 2
        print("Circle area is:", area)

    def calc_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("Circle perimeter is:", perimeter)


circle = Circle(5)

circle.calc_area()
circle.calc_perimeter()
