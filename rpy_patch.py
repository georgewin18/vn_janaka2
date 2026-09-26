import os
import re
from pathlib import Path

PROJECT_FOLDER: Path = Path(__file__).parent
AUDIO_REFERENCE: re.Pattern[str] = re.compile(r"\.(mp3|m4a|flac|wma|aac|wav)", re.IGNORECASE)


def update_rpy(file_path: Path) -> int:
    try:
        text: str = file_path.read_text(encoding="utf-8")
        new_text: str
        count: int
        new_text, count = AUDIO_REFERENCE.subn(".ogg", text)
        if count == 0:
            return 0
        file_path.write_text(new_text, encoding="utf-8")
        print(f"Updated {count} in {file_path.relative_to(PROJECT_FOLDER)}")
        return count
    except Exception as error:
        print(f"Error {file_path}: {error}")
        return 0


def main() -> None:
    scanned: int = 0
    total: int = 0
    for root, dirs, files in os.walk(PROJECT_FOLDER):
        for name in files:
            if name.lower().endswith(".rpy"):
                scanned += 1
                total += update_rpy(Path(root) / name)
    print(f"Scanned {scanned} .rpy files, replaced {total} references")


if __name__ == "__main__":
    main()