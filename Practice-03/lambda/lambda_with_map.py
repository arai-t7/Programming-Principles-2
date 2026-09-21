# Here is map() with lambda to square every number
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)