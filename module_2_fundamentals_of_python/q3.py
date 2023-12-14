# Write a Python program to get the Fibonacci series of given range

def fibo(start,end):

    fibonacci = [0,1]

    while fibonacci[-1] + fibonacci[-2] <= end:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return [num for num in fibonacci if num >= start]

start = 0
end = 100
fibonacci = fibo(start,end)

print(fibonacci)


