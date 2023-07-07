import json

data = dict({'aaa':111, 'bbbb':2222})

with open('a.json', 'w') as f:
    json.dump(data, f)