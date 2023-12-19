# Write a Python program to count the number of characters (character
# frequency) in a string
string = "Hello"
str_frequancy = {}

for i in string:
    if i in str_frequancy:
        str_frequancy[i] +=1
    else:
        str_frequancy[i] = 1

for character,count in str_frequancy.items():
    print(f"Character {character} appears {count} times in string")
