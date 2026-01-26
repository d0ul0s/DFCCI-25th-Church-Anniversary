import os

SRC = r"C:\Users\jdxrg\OneDrive\Downloads\AnnivPix"          # Downloads
DST = "SAMPLE"     # target folder

BASE_NAME = "AnnivPix"
START_NUM = 1
ZERO_PAD = 1
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

os.makedirs(DST, exist_ok=True)

files = [f for f in os.listdir(SRC) if f.lower().endswith(EXTENSIONS)]
files.sort()

for i, filename in enumerate(files, start=START_NUM):
    old_path = os.path.join(SRC, filename)

    ext = os.path.splitext(filename)[1]
    new_name = f"{BASE_NAME}{str(i).zfill(ZERO_PAD)}{ext}"
    new_path = os.path.join(DST, new_name)

    os.rename(old_path, new_path)
    print(f"{filename} -> images/{new_name}")

print("Done.")