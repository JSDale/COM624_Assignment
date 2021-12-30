import os
import matplotlib.pyplot as plt


class SaveToFiles:

    @staticmethod
    def save_graph_as_png(filename, file_path):
        filepath_exists = os.path.exists(file_path)
        if not filepath_exists:
            os.mkdir(file_path)
        plt.savefig(f'{file_path}\\{filename}.png')

    @staticmethod
    def save_to_json(raw_dataframe, filepath, filename):
        filepath_exists = os.path.exists(f'{filepath}')
        if not filepath_exists:
            os.mkdir(filepath)
        raw_dataframe.to_json(f'{filepath}\\{filename}.json')
