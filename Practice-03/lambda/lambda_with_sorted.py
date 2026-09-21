# Here is sorted() with lambda to sort students by age
students = [
    ("Arai", 18),
    ("Dana", 20),
    ("Anel", 17)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)