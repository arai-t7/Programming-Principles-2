from pathlib import Path

path = Path(input("Enter path: "))

if path.exists() and path.is_dir():
    directories = [item.name for item in path.iterdir() if item.is_dir()]
    files = [item.name for item in path.iterdir() if item.is_file()]

    print("Directories:", directories)
    print("Files:", files)
    print("All items:", directories + files)
else:
    print("Path does not exist")