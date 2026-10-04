import re

text = input("Enter text: ")
print(bool(re.fullmatch(r"ab{2,3}", text)))