import os
import matplotlib.pyplot as plt


class SaveToFiles:

    __filepath = os.getcwd()

    @staticmethod
    def save_graph_as_png(filename, file_path):
        filepath_exists = os.path.exists(file_path)
        if not filepath_exists:
            os.mkdir(file_path)
        plt.savefig(f'{file_path}\\{filename}.png')

    def save_to_json(self, raw_dataframe, filename):
        data_dir = '/Stock_Data/'
        filepath_exists = os.path.exists(f'{self.__filepath}{data_dir}')
        if not filepath_exists:
            os.mkdir(f'{self.__filepath}{data_dir}')
        raw_dataframe.to_json(f'{self.__filepath}{data_dir}{filename}')
