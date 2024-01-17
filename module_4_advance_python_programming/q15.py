# When will the else part of try-except-else be executed?
"""
If no exception will occur then else will be excecuted  

"""

try :
    result = 10/2
except ZeroDivisionError:
    print('Divide by zero is not possible')
else:
    print(result)
