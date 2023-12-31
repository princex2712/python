# Write a Python program to convert a list of characters into a string.
list_char = ['P','R','I','N','C','E']

# Method 1
def list_to_char(list_):
    return ''.join(list_)
print(list_to_char(list_char))

# Method 2
result_str = ''.join(list_char)
print()
