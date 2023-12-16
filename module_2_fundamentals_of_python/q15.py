# Write a Python program to count occurrences of a substring in a string
string = input("Enter a String: ")
sub_string = input("Enter Sub-String: ")

if sub_string.lower() in string.lower():
    print(True)
else:
    print(False)