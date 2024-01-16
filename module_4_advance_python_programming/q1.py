# What is File function in python? What is keywords to create and write
# file.
import os


"""

File function are used to perfom task on file like read and write.
'w' keyword is used to create and write in file as given in example below

"""
file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

# file_operation= open(file_location,'w')
# file_operation.write('This is my first file operation')
# file_operation.close()

# There is a short way to do this operation

with open(file_location,'w') as file:
    file.write('This is my first file operation\nThis is my first file operation on second line')

