# Write a Python program to read first n lines of a file.
import os

file_location = os.path.join('for_file_operation','first_file_operation.txt')

# Method - 1
n = 3 
with open(file_location,'r') as file:
    for i in range(n):
        print(file.readline())



# Method - 2
# n = 3
# with open(file_location,'r') as file:
#     print(file.readlines()[:n])