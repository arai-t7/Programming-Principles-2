# Here is a class using the __init__ constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Arai", 18)

print(student.name)
print(student.age)