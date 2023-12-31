# Write a Python program to check a list is empty or not.
list1 = [ ]
list2 = [23,23]

# Method-1 
def empty_list(list_):
    if len(list_) == 0:
        print('Empty List')
    else:
        print('Not Empty List')
empty_list(list1)
empty_list(list2)



# Method 2
# if not list1:
#     print('Empty List')
# else:
#     print('Not Empty List')

# if not list2:
#     print('Empty List')
# else:
#     print('Not Empty List')




# Method 3
# if not bool(list1):
#     print('Empty List')
# else:
#     print('Not Empty List')

# if not bool(list2):
#     print('Empty List')
# else:
#     print('Not Empty List')