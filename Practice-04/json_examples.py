import sys

current_folder = sys.path.pop(0)
import json
sys.path.insert(0, current_folder)


# Convert JSON string to Python dictionary
json_text = '{"name": "Arai", "age": 18}'
student = json.loads(json_text)

print(student)
print(student["name"])


# Convert Python dictionary to JSON
person = {
    "name": "Dana",
    "age": 19,
    "is_student": True
}

json_result = json.dumps(person, indent=4)
print(json_result)


# Write JSON to a file
with open("Practice-04/student.json", "w") as file:
    json.dump(person, file, indent=4)


# Read JSON from a file
with open("Practice-04/sample-data.json", "r") as file:
    data = json.load(file)


# Work with JSON data
for student in data["students"]:
    print(student["name"], student["age"])