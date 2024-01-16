# Write a Python program to read an entire text file
import os

file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

with open(file_location,'r') as file:
    print(file.read())