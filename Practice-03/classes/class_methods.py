# Here is a class with instance methods
class Calculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number


calculator = Calculator()

print(calculator.add(5, 3))
print(calculator.multiply(5, 3))