# Write a Python program to get the Factorial number of given number
num = temp = 5
fact = 1

while temp > 0 :
    fact *= temp
    temp-=1

print("Factorial of "+str(num)+" is "+str(fact))