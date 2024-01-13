# Write a Python script to concatenate following dictionaries to create a
# new one.
dict_ = {'Three': 3, 'Four': 4, 'One': 1, 'Two': 2}
dict_1 = {'Five': 5,'Six':6}

for key,val in dict_1.items():
    dict_[key] = val
print(dict_)
