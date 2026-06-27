import json
import os

OUTPUT_DIR = r"C:\Users\joshu\Downloads\fn-project\data\output"

with_band = 0
without_band = 0

for f in os.listdir(OUTPUT_DIR):
    if not f.endswith('.json'):
        continue
    with open(os.path.join(OUTPUT_DIR, f)) as file:
        d = json.load(file)
    if d.get('band_number'):
        with_band += 1
    else:
        without_band += 1

print(f"With band_number: {with_band}")
print(f"Without band_number: {without_band}")