from pathlib import Path

path = Path(input("Enter path: "))

if path.exists():
    print("Path exists")
    print("File name:", path.name)
    print("Directory:", path.parent)
else:
    print("Path does not exist")