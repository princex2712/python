# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

generated_list = [i*i for i in range(1,30) if i*i<30]
result_list = generated_list[:5] + generated_list[-5:]
print(result_list)