# Write a Python program to copy the contents of a file to another file.
import os


read_file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')
new_file_location = os.path.join(os.getcwd(), 'for_file_operation', 'copy_operation.txt')

with open(read_file_location,'r') as read_file:
    with open(new_file_location,'w') as write_file:
        write_file.writelines(read_file)
