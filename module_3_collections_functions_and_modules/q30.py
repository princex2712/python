# Write a Python program to convert a list of tuples into a dictionary
list_of_tuple = [(1,3,5,7,9),(2,4,6,8,10),(1,2,3,4,5)]



# Method - 1
# dict_of_tuple = {}
# for i in range(len(list_of_tuple)):
#     dict_of_tuple[i] = list_of_tuple[i]
# print(dict_of_tuple)

# Method - 2
dict_of_tuple = {index: tuple_ for index,tuple_ in enumerate(list_of_tuple)}
print(dict_of_tuple)
