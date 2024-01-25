# What relationship is appropriate for Student and Person?

class Person:
    
    def __init__(self,name) -> None:
        self.name= name

    def occupation(self):
        pass

class Student(Person):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def occupation(self,ocupation_name):
        self.ocupation_name = ocupation_name
        
obj = Student('Prince')
obj.occupation('Student')
print(obj.ocupation_name)