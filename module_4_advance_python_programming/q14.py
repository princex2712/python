# How many except statements can a try-except block have? Name Some
# built-in exception classes:
"""
In Python you can have multiple except based on what kind of error might occur:
Example:
"""
try:
    result = 10/0
except ZeroDivisionError:
    print('Divide by zero is not possible')
except FileNotFoundError:
    print('File Not Found')

"""
There are many built in exception in python like ZeroDivisionError, FileNotFoundError, KeyboardInterrupt etc

"""
