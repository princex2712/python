# What are oops concepts? Is multiple inheritance supported in java
"""
The four pillars of oops are 
- Encapsulation
- Abstraction
- Polymorphism
- Inheritance

No Java does supports multiple inheritance. but java support multiple interfaces

"""
class LivigThings():
    print('I am LivigThings Class')

class Animal():
    print('I am Animal Class')

class Dog(Animal,LivigThings):
    print('I am Dog Class')

obj =  Dog()