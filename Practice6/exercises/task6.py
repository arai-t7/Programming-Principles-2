from pathlib import Path
import string

folder = Path(__file__).parent / "letters"
folder.mkdir(exist_ok=True)

for letter in string.ascii_uppercase:
    file_path = folder / f"{letter}.txt"
    file_path.write_text(f"This is {letter}.txt", encoding="utf-8")

print("26 files created")