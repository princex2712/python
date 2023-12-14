# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

def new_function(first,second):
    if first == second or first + second == 5 or first - second == 5 or second - first == 5 :
        return True


num1 = int(input("Enter Your Desired Integer1: "))
num2 = int(input("Enter Your Desired Integer2: "))

print(new_function(num1,num2))