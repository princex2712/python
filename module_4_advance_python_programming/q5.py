# Write a Python program to read last n lines of a file
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

n=2
with open(file_location,'r') as file:
    line_list = file.readlines()
    for i in range(1,n+1):
        print(line_list[-1*i])
            