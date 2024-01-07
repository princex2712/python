# Write a Python program to unzip a list of tuples into individual lists
list_of_tuple = [(1,3,5,7,9),(2,4,6,8,10),(1,2,3,4,5)]
for i in range(len(list_of_tuple)):
    individual_list = list(list_of_tuple[i])
    print(individual_list)