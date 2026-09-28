import sys

current_folder = sys.path.pop(0)
import math
sys.path.insert(0, current_folder)

import random


# Built-in mathematical functions
numbers = [8, 3, 15, -4]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Absolute:", abs(-10))
print("Rounded:", round(5.678, 2))
print("Power:", pow(2, 3))

# Math module
print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Sin:", math.sin(math.pi / 2))
print("Cos:", math.cos(0))
print("Pi:", math.pi)
print("E:", math.e)

# Random module
print("Random number:", random.random())
print("Random integer:", random.randint(1, 10))

fruits = ["apple", "banana", "orange"]
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)