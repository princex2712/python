# Write a Python program to select an item randomly from a list.
import random

list1 = [2,1,45,64,3,2,2,13,1,54]

#method 1
def choose_random(list1):
     return list1[random.randrange(len(list1))]
print(choose_random(list1))



#method 2
def randomly(list1):
     return random.choice(list1)
print(randomly(list1))