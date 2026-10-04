import re

text = "Python 3 is easy. Python 3 is popular."

# Here is an example of search
print(re.search(r"Python", text).group())

# Here is an example of findall
print(re.findall(r"\d+", text))

# Here is an example of split
print(re.split(r"\s+", text))

# Here is an example of sub
print(re.sub(r"Python", "Java", text))

# Here is an example of match
print(re.match(r"Python", text).group())

# Here is an example of IGNORECASE
print(re.findall(r"python", text, re.IGNORECASE))

# Here are quantifier examples
print(re.findall(r"\w{3,6}", text))