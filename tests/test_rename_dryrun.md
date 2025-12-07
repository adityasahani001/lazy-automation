# Dry-run test plan

1. Create folder `examples/incoming` with sample files:
   - IMG_0001.JPG (with EXIF: 2023:11:15 10:01:00)  -- use a real phone photo if possible
   - IMG_0002.JPG (no EXIF)  -- you can touch the file to change mtime
   - picture.png
   - doc.txt

2. Run:
   python3 src/rename_photos.py -s examples/incoming -d examples/sorted --dry-run -r

3. Observe the printed plan — ensure names are YYYYMMDD_#### and grouped by year/month.

4. When satisfied, run without --dry-run to apply the moves.
