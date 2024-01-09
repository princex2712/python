# How can you get a random number in python?
"""
There are many way to generate number it depends on what kind of number you want to generate

"""
import random

# for genrating float number between 0,1
# 1 will be excluded
print(random.random())

# this will generate random flaot number in range
print(random.uniform(1.6,10.6))

# random int
print(random.randint(1,10))

# random integer including both 1 and 20
print(random.randint(1,20))