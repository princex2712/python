# Write a Python function to insert a string in the middle of a string.
string = input("Enter String: ")
print("New String: %s" % (string[0:len(string)//2]+' Tatakae '+string[len(string)//2:]))
