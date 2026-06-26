import json

with open('data/nations.json') as f:
    d = json.load(f)

with_coords = [x for x in d if x.get('lat')]
print(f'Records with coordinates: {len(with_coords)}')
if with_coords:
    s = with_coords[0]
    print(f'Sample: {s["nation"]}, lat={s["lat"]}, lng={s["lng"]}')