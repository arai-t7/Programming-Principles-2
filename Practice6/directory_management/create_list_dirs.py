from pathlib import Path
import os

folder = Path(__file__).parent / "example" / "documents"

folder.mkdir(parents=True, exist_ok=True)

print("Current folder:", os.getcwd())
print("Created folder:", folder)

print("Contents:")
for item in folder.parent.iterdir():
    print(item.name)