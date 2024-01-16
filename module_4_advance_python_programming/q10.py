# Write a Python program to count the frequency of words in a file
import os


file_location = os.path.join(os.getcwd(), 'for_file_operation', 'first_file_operation.txt')
frequency_of_word = {}

with open(file_location,'r') as file:
    for line in file:
        words = line.strip().split(' ')
        for word in words:
            if word not in frequency_of_word.keys():
                frequency_of_word[word] = 1
            else:
                frequency_of_word[word] += 1

for word,count in frequency_of_word.items():
    print(f'{word} : {count}')