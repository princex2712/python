# Write a Python program to calculate surface volume and area of a
# cylinder
import math

radius = float(input('Enter Radius of Cylinder:'))
height = float(input('Enter height of Cylinder:'))
surface_volume = math.pi*(radius**2)*height
surface_area = 2*math.pi*radius*height + 2*math.pi*(radius**2)
print('Surface volume of cylinder: {}\nArea of Cylinders: {}'.format(surface_volume,surface_area))