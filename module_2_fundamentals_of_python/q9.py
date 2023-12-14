# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

num1 = int(input("Enter Your Desired Integer1: "))
num2 = int(input("Enter Your Desired Integer2: "))
num3 = int(input("Enter Your Desired Integer3: "))

if num1 == num2 or num2 == num3 or num3 == num1 : 
    sum = 0
    print("Total Sum = "+str(sum))
else :
    sum = num1 +num2 + num3
    print("Total Sum = "+str(sum))