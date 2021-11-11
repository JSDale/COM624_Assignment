import json
import os

path = os.getcwd()
filepath = os.path.dirname(path)


def load_dictionary_from_json(filename):
    data_dir = '\\Stock_Data\\'
    filepath_exists = os.path.exists(f'{filepath}{data_dir}')
    if not filepath_exists:
        raise Exception(f" error loading JSON file path does not exist: {filepath}{data_dir}")

    with open(f'{filepath}{data_dir}{filename}.json') as f:
        obj = json.load(f)
        dict = obj['Adj Close']

    return dict
