import re

text = input("Enter text: ")
print(re.findall(r"\b[A-Z][a-z]+\b", text))