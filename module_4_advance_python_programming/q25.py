# Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?
"""
- Inheritance means one class occur the attribute of another class is called inheritance.
- Init is a constructor in python.
- Contructor called by itself when class object created. Constructor has no return type.

"""
# Example of inheritance and constructor

class Animal:

    def __init__(self):
        print('I am animal class contructor')
    
    def voice(self):
        pass

class Dog(Animal):

    def __init__(self):
        print('I am dog class contructor')

    def voice(self):
        print('Woof Woof!')

obj_dog = Dog()
obj_dog.voice()