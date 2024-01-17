# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.
"""
When it may chance of getting error in code snippet it should place in try code block

"""
try:
    num1 = int(input('Enter Integer number 1: '))
    num2 = int(input('Enter Integer number 2: '))
    print("Division:{}".format(num1/num2))


# if any error occur it should handle by the except

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

# finally block in both situation if error occurs or not
finally:
    print("This is finally block")