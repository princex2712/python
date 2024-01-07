# How Do You Traverse Through A Dictionary Object In Python? 
dict_ = { 1:'One',2:'Two',3:'Three'}
"""

There are many ways to traverse through dictionary as given below 


"""
# By Iterating keys
for key in dict_.keys():
    print(key,dict_[key])


# By only Iterating Values
for values in dict_.values():
    print(values)


# By Iterating items
for key,values in dict_.items():
    print(key,values)

# By only keys
for key in dict_.keys():
    print(key)


