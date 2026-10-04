import re

text = input("Enter text: ")
print(re.sub(r"[ ,.]", ":", text))