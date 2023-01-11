PI = 3.142

def circle_area(radius):
    """
    Calculate area of cirlce with given radius
    """
    area = PI*radius**2
    return area

import math

radius = int(input("Enter prefered radius: \n"))
area = circle_area(radius)
print(f"Area of circle with radius {radius} is {area}")

