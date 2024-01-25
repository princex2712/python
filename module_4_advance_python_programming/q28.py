# What relationship is appropriate for Course and Faculty?

class Faculty:

    def __init__(self,name):
        self.name = name

class Course:

    def __init__(self,course,faculty):
        self.course = course
        self.faculty = faculty

obj_faculty = Faculty('Eren Yeager')
obj_course = Course('CS',obj_faculty)
print(obj_course.course)
print(obj_course.faculty.name)

