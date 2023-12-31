# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

list1 = [2, 33, 222, 14, 25]

# Method-1 # 
list1.pop()
print(list1)

## Method-2 ## 
# del list1[len(list1)-1]
# print(list1)

## Method-3 ## 
# print(list1[:-1])

## Method-4 ## 
# list1 = list1[:-1]
# print(list1)
