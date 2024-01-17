# Write python program that user to enter only odd numbers, else will
# raise an exception.
class OddNumberExcept(Exception):
    pass
flag = True
while(flag):
    try:
        num = int(input('Enter Odd Number: '))
        if num % 2 == 0:
            raise OddNumberExcept("Only Odd values are allowed")
        else:
            flag = False
    except ValueError as e:
        print(e)
print("You Entered odd number")