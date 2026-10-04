import re

text = input("Enter text: ")
print(re.split(r"(?=[A-Z])", text))