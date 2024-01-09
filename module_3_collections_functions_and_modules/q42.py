# Write a Python program to print all unique values in a dictionary
d1 = {'a': 100, 'b': 200, 'c':300, 'd':200, 'e':100} 


# Method-1
# unq_values= []
# for values in d1.values():
#     if values not in unq_values:
#         unq_values.append(values)
# print(unq_values)
    

# Method-2
set_of_values = {val for val in d1.values()}
print(set_of_values)