# Here is the difference between class and instance variables
class Student:
    university = "KBTU"

    def __init__(self, name):
        self.name = name


first_student = Student("Arai")
second_student = Student("Dana")

print(first_student.name, first_student.university)
print(second_student.name, second_student.university)

Student.university = "New University"

print(first_student.university)
print(second_student.university)