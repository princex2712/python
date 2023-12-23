# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.
string = input("Enter Your String: ")

if 'not' and 'poor' in string.lower():
    if string.lower().find('not') < string.lower().find('poor'):
        new_str = string[0:string.lower().find('not')] +'good'+ string[string.lower().find('poor')+4:]
        print(new_str.title())
    else:
        print("Not keyword accuring after poor")
else:
    print("Your String not containing substring \'not...poor\'")
    