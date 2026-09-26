import os
import re
from pathlib import Path

PROJECT_FOLDER: Path = Path(__file__).parent
SCENE_BLOCK: re.Pattern[str] = re.compile(r"(?m)^([ \t]*scene\b[^\n]*:\n(?:[ \t]+[^\n]*\n?)+)")
ZOOM_LINE: re.Pattern[str] = re.compile(r"^([ \t]*)zoom\s+[0-9.]+[ \t]*$", re.MULTILINE)


def zoom_replace(match: re.Match[str]) -> str:
    indent: str = match.group(1)
    return f"{indent}size (config.screen_width, config.screen_height)\n{indent}truecenter"


def scale_scene_blocks(text: str) -> tuple[str, int]:
    count: int = 0

    def block_replace(match: re.Match[str]) -> str:
        nonlocal count
        new_block: str
        replaced: int
        new_block, replaced = ZOOM_LINE.subn(zoom_replace, match.group(1))
        count += replaced
        return new_block

    return SCENE_BLOCK.sub(block_replace, text), count


def update_rpy(file_path: Path) -> int:
    try:
        text: str = file_path.read_text(encoding="utf-8")
        new_text: str
        count: int
        new_text, count = scale_scene_blocks(text)
        if count == 0:
            return 0
        file_path.write_text(new_text, encoding="utf-8")
        print(f"Replaced {count} zoom in {file_path.relative_to(PROJECT_FOLDER)}")
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
    print(f"Scanned {scanned} .rpy files, replaced {total} zoom lines")


if __name__ == "__main__":
    main()