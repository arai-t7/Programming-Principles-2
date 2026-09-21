# Here is method overriding
class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog says woof")


animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()