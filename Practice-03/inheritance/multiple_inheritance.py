# Here is multiple inheritance
class Student:
    def study(self):
        print("Student is studying")


class Athlete:
    def train(self):
        print("Athlete is training")


class SportsStudent(Student, Athlete):
    pass


person = SportsStudent()
person.study()
person.train()