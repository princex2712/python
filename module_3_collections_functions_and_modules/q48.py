# Write a Python function to calculate the factorial of a number (a
# nonnegative integer)
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(5))
