# Write a Python script to merge two Python dictionaries
dict_1 = { 1:'One',2:'Two',3:'Three'}
dict_2 = { 4:'Four',5:'Five',6:'Six'}

# Method-1
# merged_dict = {}
# for key,val in dict_1.items():
#     merged_dict[key] = val
# for key,val in dict_2.items():
#     merged_dict[key] = val
# print(merged_dict)

# Method-2
# dict_1.update(dict_2) 
# print(dict_1)

# Method-3
merged_dict = dict(list(dict_1.items())+list(dict_2.items()))
print(merged_dict)