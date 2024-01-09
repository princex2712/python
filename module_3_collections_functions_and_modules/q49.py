# Write a Python function to check whether a number is in a given range
num = 3
given_range = input('Enter range seperated by comma: ').split(',')

print("Yes, {} is in range".format(num)) if num in range(int(given_range[0]),int(given_range[1])) else print("No, {} is not in range".format(num))
print("Yes, {} is in range".format(num)) if int(given_range[0])<=num<=int(given_range[1])-1 else print("No, {} is not in range".format(num))