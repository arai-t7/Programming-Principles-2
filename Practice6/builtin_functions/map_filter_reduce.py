from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Возвести числа в квадрат
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

# Оставить только чётные числа
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Найти произведение всех чисел
product = reduce(lambda first, second: first * second, numbers)
print("Product:", product)

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted:", sorted(numbers, reverse=True))