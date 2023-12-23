# Write a Python function to reverses a string if its length is a multiple of
# 4.
string = input("Enter String: ")
if len(string)%4==0:
    print(string[::-1])
else:
    print("Length is not a multiple of 4")