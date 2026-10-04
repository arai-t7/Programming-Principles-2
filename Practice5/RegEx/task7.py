import re

text = input("Enter snake case: ")

result = re.sub(
    r"_([a-z])",
    lambda match: match.group(1).upper(),
    text
)

print(result)