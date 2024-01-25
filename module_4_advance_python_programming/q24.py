# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle
from math import pi

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi*self.radius**2
    
    def perimeter(self):
        return 2*pi*self.radius
    
obj_circle = Circle(10)
print(f'Area: {obj_circle.area()}')
print(f'Perimeter: {obj_circle.perimeter()}')