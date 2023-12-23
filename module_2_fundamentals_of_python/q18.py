# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.
string = input("Enter Your String: ")

if len(string) < 3:
    print("String length Should be 3 or above")
    new_str = string
else:
    if string.lower().endswith('ing'):
        new_str = string + 'ly'
    else:
        new_str = string + 'ing'
print(f"Your String \"{new_str.title()}\"")
