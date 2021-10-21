import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import os


def plot_rolling_average(close_px, moving_average):
    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__

    style.use('ggplot')

    close_px.plot(label='AAPL')
    moving_average.plot(label='mavg')
    plt.legend()
    filepath = os.getcwd()
    plt.savefig(filepath + '/rolling_graph.png')
