# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

new_str1 = str1[1] + str1 [0] + str1[2:] +' '+ str2[1] + str2[0] + str2[2:]

print(new_str1)