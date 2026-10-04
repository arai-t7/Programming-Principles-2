import re

text = input("Enter text: ")
print(re.findall(r"\b[a-z]+_[a-z]+\b", text))