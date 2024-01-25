# What is Instantiation in terms of OOP terminology?
"""
Instantiation is a process of creating instance of a class.It involves the memory allocation and initializing attributes using constructor.

"""

class Hello:

    def __init__(self,company,car):
        self.company = company
        self.car = car
obj_hello = Hello('BMW','M5')
print(obj_hello.company,end=" ")
print(obj_hello.car)

        