import os
from pathlib import Path
from PIL import Image
import subprocess

PROJECT_FOLDER: Path = Path(__file__).parent
AUDIO_EXTENSIONS: tuple[str, ...] = (".mp3", ".wav", ".m4a", ".flac", ".wma", ".aac")

def convert_audio(file_path: Path) -> None:
    output_path: Path = file_path.with_suffix(".ogg")
    print(f"Converting: {file_path.name}")
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(file_path), "-c:a", "libvorbis", "-b:a", "128k", str(output_path)],
            check=True,
            capture_output=True,
        )
        file_path.unlink()
    except subprocess.CalledProcessError as error:
        print(f"Error converting {file_path}: {error.stderr.decode(errors='ignore')}")


def compress_png(file_path: Path) -> None:
    print(f"Compressing: {file_path.name}")
    try:
        with Image.open(file_path) as image:
            new_size = (max(1, image.width // 4), max(1, image.height // 4))
            resized = image.resize(new_size, Image.Resampling.LANCZOS)
            resized.save(file_path, format="PNG", optimize=True)
    except Exception as error:
        print(f"Error compressing {file_path}: {error}")


def process_file(file_path: Path) -> None:
    suffix = file_path.suffix.lower()
    if suffix in AUDIO_EXTENSIONS:
        convert_audio(file_path)
    elif suffix == ".png":
        compress_png(file_path)


def main() -> None:
    if not PROJECT_FOLDER.exists():
        print(f"Directory '{PROJECT_FOLDER}' does not exist")
        return

    for root, dirs, files in os.walk(PROJECT_FOLDER):
        for name in files:
            process_file(Path(root) / name)

    print("Done")


if __name__ == "__main__":
    main()