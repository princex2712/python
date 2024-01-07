# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15. 
list_of_keys = [ i for i in range(1,15)]
dict_ = dict.fromkeys(list_of_keys)
print(dict_)    