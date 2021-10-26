import os
import matplotlib.pyplot as plt


class SaveToFiles:

    __filepath = os.getcwd()

    def save_graph_as_png(self, filename):
        plt.savefig(f'{self.__filepath}/Stock_Data/{filename}')
