# Here is super() calling the parent constructor
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student = Student("Arai", 2)

print(student.name)
print(student.course)