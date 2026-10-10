from pathlib import Path

file_path = Path(__file__).parent / "sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)