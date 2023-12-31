#  Differentiate between append () and extend () methods?
"""
With the help of append you can only append able to add one element at last position in list
for ex-

"""
list_ = [1,2,3,4,5,6]
print(list_)
list_.append(7)
print(list_)

"""
And the other hand extend method can able to add all element which are iterable like list or tuple
for ex

"""
list_2 = [1,2,3]
print(list_2)
list_2.extend(i for i in range(4,8))
print(list_2)