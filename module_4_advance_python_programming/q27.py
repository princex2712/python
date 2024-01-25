# What is used to check whether an object o is an instance of class A?
"""
You can check it as given below:

"""

class Hello:

    def __init__(self,company,car):
        self.company = company
        self.car = car
obj_hello = Hello('BMW','M5')
print(isinstance(obj_hello,Hello))