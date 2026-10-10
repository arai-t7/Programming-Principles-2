from pathlib import Path
import os

path = Path(input("Enter file path: "))

if not path.exists():
    print("File does not exist")
elif not path.is_file():
    print("The path is not a file")
elif not os.access(path, os.W_OK):
    print("No permission to delete the file")
else:
    path.unlink()
    print("File deleted")