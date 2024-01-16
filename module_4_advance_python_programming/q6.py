# Write a Python program to read a file line by line and store it into a list
import os

file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

with open(file_location,'r') as file:
    line_list = file.readlines()
print(line_list)