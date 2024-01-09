# How Many Basic Types Of Functions Are Available In Python?
"""
There are several basic funtions are availible in pyhton built in library.
such as given below:

"""
# built in funtion
print('Hello')

# user define funtion
a = 10
b = 15
def sum(a,b):
    return a+b
print(sum(a,b))

# lambda funtion
mul = lambda x, y: x*y


# recursion function
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(5))


# generator function

def generator():
    for i in range(6):
        yield i

get_instance = generator()
print(next(get_instance))
print(next(get_instance))
print(next(get_instance))
print(next(get_instance))
print(next(get_instance))
print(next(get_instance))

