import json
import os


def load_dictionary_from_json(filepath):
    filepath_exists = os.path.exists(f'{filepath}.json')
    if not filepath_exists:
        raise Exception(f" error loading JSON file path does not exist: {filepath}.json")

    with open(f'{filepath}.json') as f:
        obj = json.load(f)
        dict = obj['Adj Close']

    return dict
