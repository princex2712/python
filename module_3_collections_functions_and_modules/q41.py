# Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}

# Method - 1
# for key,val in d1.items():
#     if key in d2:
#         d1[key] += d2[key]
# for key in d2.keys():
#     if key not in d1:
#         d1[key] = d2[key]
# print(dict(sorted(d1.items(),key= lambda item:item[1],reverse=True)))


# Method - 2
merged_dict = {}
for key in set(d1.keys() | d2.keys()):
    merged_dict[key] = d1.get(key,0) + d2.get(key,0)
print(merged_dict)
