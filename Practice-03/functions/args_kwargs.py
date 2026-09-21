# Here is a function using *args
def calculate_total(*numbers):
    return sum(numbers)


# Here is a function using **kwargs
def show_student(**student):
    for key, value in student.items():
        print(key, ":", value)


print(calculate_total(10, 20, 30))
show_student(name="Arai", age=18, city="Almaty")