# Write a Python program to read a file line by line store it into a variable.
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

with open(file_location,'r') as file:
    file_content = ""
    for content in file:
        file_content +=content
print(file_content)