names = ["Anna", "Arai", "Dana"]
ages = [18, 19, 20]

# enumerate добавляет порядковый номер
for number, name in enumerate(names, start=1):
    print(number, name)

# zip объединяет два списка
for name, age in zip(names, ages):
    print(name, age)

# Преобразование типов
number_text = "25"

number = int(number_text)
decimal = float(number_text)
new_text = str(number)

print(type(number))
print(number, decimal, new_text)