# Write a Python program to read a random line from a file.
import random

# i have 50 + quetions so it will take any of these and return random line
file_location = 'q'+str(random.randrange(1,51))+'.py'

with open(file_location,'r') as file:
    total_line = sum(1 for _ in file)
    file.seek(0)
    random_line = random.randrange(1,total_line)
    
    for line_index,line in enumerate(file):
        if line_index==random_line:
            print('Line No {} In {} :'.format(line_index+1,file_location)+line.strip())


