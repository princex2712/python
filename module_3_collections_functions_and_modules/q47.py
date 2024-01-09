#  Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'
# Expected output:
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
string = "princepatel"


# Method - 1 
# dict_ = {}
# for char in string:
#     if char in dict_.keys():
#         dict_[char] +=1
#     else:
#         dict_[char] = 1
# print(dict_)



# Method - 2 
# dict_ = dict.fromkeys(string)
# for key,val in dict_.items():
#     dict_[key] = string.count(key)
# print(dict_)


# Method - 3
dic_ = {}
for char in string:
    dic_[char] = dic_.get(char,0)+1
print(dic_)