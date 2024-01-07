#  Write a Python program to find the repeated items of a tuple. 
tuple_ = (1,2,3,4,5,6,7,8,4,1,9,3)

# method - 1
# repeated_items = []
# for i in tuple_:
#     if tuple_.count(i)>1 and i not in repeated_items:
#         repeated_items.append(i)
# print(repeated_items)

# method - 2
repeated_items = {item for item in tuple_ if tuple_.count(item)>1}
print(list(repeated_items))

