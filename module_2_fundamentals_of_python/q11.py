# Write a python program to sum of the first n positive integers.
n = 5
temp = n
sum = 0
while temp > 0:
    sum+=temp
    temp-=1

print("Sum Of First "+str(n)+" Numbers= "+str(sum))