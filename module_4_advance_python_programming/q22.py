# How to Define a Class in Python? What Is Self? Give An Example Of
# A Python Class
"""
You Can Define class as below and as per python documentation in class name first letter should be capital:

"""
class YourClassName:

    def __init__(self): #self keyword is a first parameter of every method define in class. It is instance of class and it used to modify and access attribute
        print('I am constructor')

obj = YourClassName()