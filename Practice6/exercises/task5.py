from pathlib import Path

items = ["Apple", "Banana", "Orange", "Grape"]
file_path = Path(__file__).parent / "list.txt"

with open(file_path, "w", encoding="utf-8") as file:
    for item in items:
        file.write(item + "\n")

print("List written to file")