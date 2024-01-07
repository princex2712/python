# Write a Python program to map two lists into a dictionary
keys = [ 1,2,3,4,5]
values = [ 'One','Two','Three','Four','Five']

#  Method-1
dict_ = {}
for i in range(len(keys)):
    dict_[keys[i]] = values[i] 
print(dict_)

#  Method-2
# dict_= dict.fromkeys(keys)
# i=0
# for key in dict_.keys():
#     dict_[key] = values[i]
#     i+=1
# print(dict_)

# Method-3
# dict_ = dict(zip(keys,values))
# print(dict_)