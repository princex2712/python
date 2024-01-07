# Write a Python program to remove an empty tuple(s) from a list of tuples. 
list_of_tuple = [(1,3,5,7,9),(2,4,6,8,10),(),(1,2,3,4,5),()]

for index,tuple_ in enumerate(list_of_tuple):
    if len(tuple_) == 0:
        list_of_tuple.pop(index)
print(list_of_tuple)