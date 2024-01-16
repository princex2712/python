# Write a Python program to write a list to a file.
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'writeList_in_file.txt')
list_of_line = ['I am writing first line form list\n','I am writing second line form list\n','I am writing third line form list\n']
with open(file_location,'w') as file:
    file.writelines(list_of_line)

