from pathlib import Path

path = Path(input("Enter file path: "))

if path.exists() and path.is_file():
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("Number of lines:", len(lines))
else:
    print("File does not exist")