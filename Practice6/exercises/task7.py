from pathlib import Path
import shutil

folder = Path(__file__).parent
source = folder / "source.txt"
destination = folder / "destination.txt"

source.write_text("Text from source file", encoding="utf-8")

shutil.copyfile(source, destination)

print("File contents copied")