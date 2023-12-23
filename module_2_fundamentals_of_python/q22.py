# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.
string = input("Enter String: ")

if len(string) < 2 :
    new_str = ''
    print("Given String has length of less than 2.")
    print("New String: %s" % (new_str))
else:
    new_str = string[0:2] + string[-2::]
    print("New String: %s" % (new_str))