# Write a Python program to find the second smallest number in a list

list1 = [1,45,64,3,13,1,54]

# Method 1
def second_smallest(list):
    small = min(list)
    list.sort()
    for i in list:
        if i > small:
            return i
print(second_smallest(list1))


# Method 2
def second_smallest_(list):
    new_list=set(list)
    new_list.remove(min(list))
    return min(new_list)
print(second_smallest_(list1))



#Method 3
def second_smallest__(list12):
    uniq_elements = list(set(list12))
    uniq_elements.sort()
    return list(uniq_elements)[1]
print(second_smallest__(list1))