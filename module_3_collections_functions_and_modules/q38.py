# Write a Python program to check multiple keys exists in a dictionary
list_of_keys = [ i for i in range(1,10)]
dict_ = { 1:'One',2:'Two',3:'Three'}

for key in list_of_keys:
    if key in dict_:
        print('Key:{} already exists in dictionary'.format(key))
    else:
        print('Key:{} not in dictionary'.format(key))                    