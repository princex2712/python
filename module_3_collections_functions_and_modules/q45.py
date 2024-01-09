# Write a Python program to find the highest 3 values in a dictionary
d1 = {'a': 200, 'b': 800, 'c':500, 'd':450, 'e':100, 'f':1000, 'g':560}

# max_three = sorted([val for val in d1.values()])
# max_three = max_three[:-4:-1]
# print(max_three)  

max_three = sorted([val for val in d1.values()],reverse=True)[:3]
print(max_three[::-1])  
