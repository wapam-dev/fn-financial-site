import json

with open('data/nations.json') as f:
    d = json.load(f)

results = [x for x in d if 'red pheasant' in x.get('nation', '').lower()]
print(f'Found {len(results)} records:')
for r in results:
    print(f"  {r['nation']} {r['fiscal_year']} — score:{r.get('health_score')} lat:{r.get('lat')} lng:{r.get('lng')}")