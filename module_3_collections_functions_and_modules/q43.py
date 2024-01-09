# Why Do You Use the Zip () Method in Python?
"""

There are sevaral problem which can be solved using zip() function very easily like example below:
If You have to create dictionary where key and values has saperate list

"""
key = [1,2,3,4]
values = ['a','b','c','d']

dict_ = dict(zip(key,values))
print(dict_)

"""
Also You can unzip the zipped elements

"""
key = [1,2,3,4]
values = ['a','b','c','d']

zipped = zip(key,values)
unzipped = zip(*zipped)
print(list(unzipped))