# Write a Python program to remove duplicates from a list.
list1 = [2,1,45,64,3,2,2,13,1,54]

# Method-1 ##
new_list = []
new_list.extend(i for i in list1 if i not in new_list)
print(new_list)
           


## Method-2 ##
# new_list = []

# for item in list1:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)

## Method-3 ##
# set1 = set(list1)
# new_list = list(set1)
# print(new_list)

## Method-4 ##
# new_list = list(dict.fromkeys(list1))
# print(new_list)
