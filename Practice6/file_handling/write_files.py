from pathlib import Path

folder = Path(__file__).parent
file_path = folder / "sample.txt"

# w — создать файл или перезаписать его
with open(file_path, "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")

# a — добавить текст в конец
with open(file_path, "a", encoding="utf-8") as file:
    file.write("Third line\n")

print("File created and updated")