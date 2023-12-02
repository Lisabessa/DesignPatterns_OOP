# Mediator - contains the logic of interaction of other classes
class Course:
    def show_course(self, user, course_name):
        print(user + ' is taking the course ' + course_name)


# Colleague - a class whose instances want to interact with each other
class Student:
    def __init__(self, name):
        self.name = name
        self.course = Course()  # mediator is an additional link

    def setCourse(self, course_name):
        self.course.show_course(self.name, course_name)


student1 = Student('Sanek')
student2 = Student('Anna')
student3 = Student('Max')
student1.setCourse('Design patterns in OOP')
student2.setCourse('System programming in Python')
student3.setCourse('Design patterns in OOP')