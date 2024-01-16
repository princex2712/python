# Write a Python program to append text to a file and display the text.
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')

with open(file_location,'a+') as file:
    file.write('\nAppending Text On Third Line')

    # to move cursor at the start of the file
    file.seek(0)
    print(file.read())
