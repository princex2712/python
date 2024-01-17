# When is the finally block executed?
"""
Finnally block will excecute in any condition if try will execute without error or it gets exception
"""
try:
    result = 10/2
except ZeroDivisionError as e:
    print(e)
finally:
    print("I will Excecute in any condition")