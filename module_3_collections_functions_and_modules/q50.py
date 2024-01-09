# Write a Python function to check whether a number is perfect or not.
def perfect(num):
    if num <=0:
        return "{} is not a Perfect Number".format(num)
    divisor = {1}
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            divisor.add(i)
            divisor.add(num/i)
    if sum(divisor)==num:
        return "{} is Perfect Number".format(num)
    return "{} is not a Perfect Number".format(num)
print(perfect(496))