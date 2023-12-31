# Write a Python function that takes two lists and returns true if they have
# at least one common member.

list1 = input('Enter Your Elements of List 1 sapareted by comma:').split(',')
list2 = input('Enter Your Elements of List 2 sapareted by comma:').split(',')

# Method 1
def common_chk(list1_,list2_):
    for i in list1_:
        if i in list2_:
            return True
    return False

print(common_chk(list1,list2))


# Method 2
# def sort_common_chk(list_1,list_2):
#     if bool(set(list_1) & set(list_2)): #Intersection using & operator
#         print(True)
#     else:
#         print(False)
# sort_common_chk(list1,list2)



# Method 3
# def sort_common_chk1(list1,list2):
#     return any(item in list1 for item in list2)
# print(sort_common_chk1(list1,list2))