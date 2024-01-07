# Write a Python script to check if a given key already exists in a
# dictionary. 
dict_ = { 1:'One',2:'Two',3:'Three'}
given_key = int(input('Enter Key: '))

if given_key in dict_.keys():
    print("Key Already Exists")
else:
    print("Key Not Found")