import json


def open_json(destination):
    with open(f'{destination}.json') as f:
        data = json.load(f)
    return data


def dump_json(destination, data):
    with open(f'{destination}.json', 'w') as f:
        json.dump(data, f, indent=4)


