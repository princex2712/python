# How Do You Check The Presence Of A Key In A Dictionary?
"""

Dictionary has method dict.keys() which can iterate key with the help of that method we can check for persence of key.  

"""
dict_ = { 1:'One',2:'Two',3:'Three'}


# print keys from dictionary
for key in dict_.keys():
    print(key)

# if you want to check presence of key 
check_key = 3
print(True) if check_key in dict_.keys() else print(False) 