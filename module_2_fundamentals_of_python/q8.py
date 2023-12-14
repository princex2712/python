# Write a Python program to test whether a passed letter is a vowel or
# not.

input_char = input("Enter Desired Letter: ")
vowel = ['a','e','i','o','u']

if  input_char.lower() in vowel :
    print("\n"+input_char+" Is Vowel")
else :
    print("\n"+input_char+" Is Not a Vowel")
 