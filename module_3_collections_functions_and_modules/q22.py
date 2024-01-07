# Write a Python program to check whether an element exists within a
# tuple
tuple_ =(2,4,5,6,78,5)
element_to_search = int(input('Enter Element:'))
ans = list(tuple_).count(element_to_search)
print(True) if ans>=1 else print(False)