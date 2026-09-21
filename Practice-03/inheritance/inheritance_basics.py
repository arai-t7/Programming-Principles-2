# Here is basic inheritance
class Person:
    def speak(self):
        print("Person is speaking")


class Student(Person):
    def study(self):
        print("Student is studying")


student = Student()
student.speak()
student.study()