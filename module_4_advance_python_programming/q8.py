# Write a python program to find the longest words.
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')
with open(file_location,'r') as file:
    longest_word = ""
    for line in file:
        words_list = line.strip().split(' ')
        for word in words_list:
            if len(word)>len(longest_word):
                longest_word = word 
print(longest_word)