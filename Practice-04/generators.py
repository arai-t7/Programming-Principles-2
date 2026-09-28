# Iterator using iter() and next()
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Custom iterator
class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        number = self.current
        self.current += 1
        return number


for number in Counter(5):
    print(number)


# Generator function using yield
def even_numbers(limit):
    for number in range(0, limit + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)


# Generator expression
squares = (number ** 2 for number in range(1, 6))

print(list(squares))