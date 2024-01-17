# Can one block of except statements handle multiple exception?
"""
Yes, one block of except statements handle multiple exception

"""
try:
    result = 10/0
except (ValueError,ZeroDivisionError) as e:
    print(e)
