# Write a Python program to replace last value of tuples in a list.

list_ = [(1,3,5,7,9),(2,4,6,8,10),(1,2,3,4,5)]
replace_value = int(input('Enter New Value to Replace:'))

# Method - 1 
# for i in range(len(list_)) :
#     tuple_ = list(list_[i])
#     tuple_.pop()
#     tuple_.append(replace_value)
#     list_[i] = tuple(tuple_)
# print(list_)

# Method - 2
for i in range(len(list_)):
    tuple_ = list(list_[i])
    tuple_[-1] = replace_value
    list_[i] = tuple(tuple_)
print(list_)