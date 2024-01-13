# Write a Python program to calculate the area of a trapezoid
short_base = float(input("Enter short base value: "))
long_base = float(input("Enter long base value: "))
height = float(input("Enter height base value: "))
area = (short_base+long_base)*height/2
print("Area of trapezoid: {}".format(area))