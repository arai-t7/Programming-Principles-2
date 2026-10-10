from pathlib import Path
import shutil

folder = Path(__file__).parent
source = folder / "sample.txt"
backup = folder / "sample_backup.txt"

if source.exists():
    shutil.copy(source, backup)
    print("Backup created")

# Удаление резервной копии
if backup.exists():
    backup.unlink()
    print("Backup deleted")