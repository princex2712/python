# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd

dict_ = {'1': ['a','b'], '2': ['c','d']}
combinations = []
for key,val in dict_.items():
    for key1,val1 in dict_.items():
        if key != key1:
            for char1 in val:
                for char2 in val1:
                    combinations.append(char1+char2)
print(combinations[0:len(dict_)*2])