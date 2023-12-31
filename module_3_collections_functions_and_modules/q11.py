# Write a Python function that takes a list and returns a new list with unique
# elements of the first list

list1=[1,2,3,4,5,4,3,2,1]

# Method-1
def unique(list_):
    return [item for index,item in enumerate(list_) if item not in list_[:index]]
print(unique(list1))

# Method-2
def unique_list(list__):
    return list(set(list__))
print(unique_list(list1))