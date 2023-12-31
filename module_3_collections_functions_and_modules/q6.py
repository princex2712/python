# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings
input_strings = ['Reyna','Hi','O','Razer','Omen','Jett','Brimstone','Neon']
count_of_str = 0

for i in input_strings:
    if len(i)>=2 and i[0].lower() == i[-1].lower():
        count_of_str += 1 
print(count_of_str)

print(sum(1 for i in input_strings if len(i)>=2 and i[0].lower() == i[-1].lower()))