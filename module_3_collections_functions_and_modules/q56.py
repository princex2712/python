# How will you set the starting value in generating random numbers?
import random

# with using seed you can set starting value in random number
random.seed(23) 
num1 = random.random()
num2 = random.randrange(1,100)
print(num1)
print(num2)