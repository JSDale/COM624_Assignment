import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import os


filepath = os.getcwd()


def plot_rolling_average(close_px, moving_average):
    mpl.rc('figure', figsize=(20, 15))
    mpl.__version__

    style.use('ggplot')

    close_px.plot(label='AAPL')
    moving_average.plot(label='mavg')
    plt.legend()
    plt.savefig(filepath + '/Stock_Data/rolling_graph.png')
