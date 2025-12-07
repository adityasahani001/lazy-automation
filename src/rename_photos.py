#!/usr/bin/env python3
"""
rename_photos.py
Simple tool to rename and organize a folder of photos/files:
- Tries to read EXIF DateTimeOriginal (if image and has EXIF)
- Falls back to file modification time
- Renames to: YYYYMMDD_NNNN.ext (NNNN sequence per-day)
- Moves into: <output_dir>/<YYYY>/<MM>/
- Supports dry-run and logging
Usage:
    python3 src/rename_photos.py --source /path/to/input --dest /path/to/output --dry-run
"""

from pathlib import Path
from PIL import Image, ExifTags
import argparse
import datetime
import logging
import shutil
from collections import defaultdict

EXIF_DATETIME_TAGS = ("DateTimeOriginal", "DateTime", "DateTimeDigitized")

def get_exif_datetime(filepath: Path):
    try:
        img = Image.open(filepath)
        exif = img._getexif()
        if not exif:
            return None
        tag_map = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
        for t in EXIF_DATETIME_TAGS:
            if t in tag_map:
                raw = tag_map[t]
                try:
                    dt = datetime.datetime.strptime(raw, "%Y:%m:%d %H:%M:%S")
                    return dt
                except Exception:
                    continue
        return None
    except Exception:
        return None

def get_file_mtime(path: Path):
    ts = path.stat().st_mtime
    return datetime.datetime.fromtimestamp(ts)

def safe_create_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Rename and organize photos/files by date.")
    parser.add_argument("--source", "-s", required=True, type=Path, help="Source folder containing files")
    parser.add_argument("--dest", "-d", required=True, type=Path, help="Destination root folder")
    parser.add_argument("--ext", "-e", nargs="*", default=None, help="Optional: limit to extensions, e.g. .jpg .png")
    parser.add_argument("--dry-run", action="store_true", help="Do not actually move/rename, only print actions")
    parser.add_argument("--recursive", "-r", action="store_true", help="Process files recursively")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s")
    src = args.source
    dst_root = args.dest
    if not src.exists() or not src.is_dir():
        logging.error("Source '%s' does not exist or is not a directory.", src)
        return

    if args.ext:
        exts = {ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in args.ext}
    else:
        exts = None

    if args.recursive:
        files = [p for p in src.rglob("*") if p.is_file()]
    else:
        files = [p for p in src.iterdir() if p.is_file()]

    seq = defaultdict(int)
    actions = []

    for f in sorted(files):
        if exts and f.suffix.lower() not in exts:
            logging.debug("Skipping (extension filter): %s", f)
            continue

        dt = None
        if f.suffix.lower() in {".jpg", ".jpeg", ".tiff", ".png"}:
            dt = get_exif_datetime(f)

        if dt is None:
            dt = get_file_mtime(f)

        date_str = dt.strftime("%Y%m%d")
        year = dt.strftime("%Y")
        month = dt.strftime("%m")

        seq[date_str] += 1
        seqnum = f"{seq[date_str]:04d}"

        new_name = f"{date_str}_{seqnum}{f.suffix.lower()}"
        dest_dir = dst_root / year / month
        dest_path = dest_dir / new_name

        actions.append((f, dest_path))
        logging.info("Will move: %s -> %s", f, dest_path)

    for src_path, dest_path in actions:
        safe_create_dir(dest_path.parent)
        if args.dry_run:
            logging.info("[DRY RUN] mv %s -> %s", src_path, dest_path)
        else:
            final_path = dest_path
            i = 1
            while final_path.exists():
                final_path = dest_path.with_name(dest_path.stem + f"_{i}" + dest_path.suffix)
                i += 1
            logging.info("Moving: %s -> %s", src_path, final_path)
            shutil.move(str(src_path), str(final_path))

    logging.info("Done. Processed %d files.", len(actions))

if __name__ == "__main__":
    main()
