import json

def read_json(path_to_json):
    with open(path_to_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(path_to_json, data):
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)
