# Write a Python script to sort (ascending and descending) a dictionary by value. 
dict_ = {'Three': 3, 'Four': 4, 'One': 1, 'Two': 2}

sorted_dict_asc = dict(sorted(dict_.items(),key=lambda item : item[1]))
sorted_dict_dsc = dict(sorted(dict_.items(),key=lambda item : item[1],reverse=True))
print(sorted_dict_asc)
print(sorted_dict_dsc)



