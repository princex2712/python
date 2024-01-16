# Write a Python program to count the number of lines in a text file
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

with open(file_location,'r') as file:
    count = 0
    for line in file:
        count+=1
print(f'Numbers of line: {count}')