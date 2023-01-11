PI = 3.142

def circle_area(radius):
    """
    Calculate area of cirlce with given radius
    """
    area = PI*radius**2
    return area



radius = int(input("Enter prefered radius: \n"))
unit = input("What units are you working in? \n")
unit_sqr ="{}²".format(unit)
area = circle_area(radius)
print(f"Area of circle with radius {radius} is {area}"+ unit_sqr)

