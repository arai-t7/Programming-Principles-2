from pathlib import Path
import shutil

base = Path(__file__).parent
source_folder = base / "source"
destination_folder = base / "destination"

source_folder.mkdir(exist_ok=True)
destination_folder.mkdir(exist_ok=True)

file_path = source_folder / "example.txt"
file_path.write_text("Hello Python", encoding="utf-8")

shutil.copy(file_path, destination_folder / "copy.txt")
print("File copied")

shutil.move(file_path, destination_folder / "example.txt")
print("File moved")