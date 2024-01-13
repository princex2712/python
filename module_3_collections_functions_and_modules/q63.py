# Write a Python program to returns sum of all divisors of a number
def sumofdivisor(num):
    divisor = set()
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            divisor.add(i)
            divisor.add(num//i)
    return sum(divisor)
print(sumofdivisor(6))


