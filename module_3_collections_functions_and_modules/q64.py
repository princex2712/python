# Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.

# Method - 1
# def max_min(num):
#     digit = []
#     while(num>0):
#         new_digit = num%10
#         digit.append(new_digit)
#         num = num//10
#     return max(digit),min(digit)
# decimal =abs(int(input('Enter Decimal number: ')))
# print('Maximum Digit: {}\nMinimum Digit: {}'.format(*max_min(decimal)))


# Method - 2
def short(num):
    digit = [int(i) for i in str(num)]
    return max(digit),min(digit)

decimal =abs(int(input('Enter Decimal number: ')))
print('Maximum Digit: {}\nMinimum Digit: {}'.format(*short(decimal)))
