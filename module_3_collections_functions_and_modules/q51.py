# Write a Python function that checks whether a passed string is
# palindrome or not
def isPalindrome(string):
    if string.lower() == string[::-1].lower():
        return "{} is Palindrome".format(string)
    return "{} is not Palindrome".format(string)
print(isPalindrome('hello'))