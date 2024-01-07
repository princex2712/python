# How will you create a dictionary using tuples in python?

# in list of tuple is like (key:value)
list_of_tuple = [(1,'One'),(2,'Two'),(3,'Three')]
# Method-1
# dict_ = { key:value for key,value in list_of_tuple}
# print(dict_)


# Method-2
dict_ = dict(list_of_tuple)
print(dict_)


# Method-3
# dict_ = {list_of_tuple[index][0]:list_of_tuple[index][1] for index,value in enumerate(list_of_tuple)}
# print(dict_)