import matplotlib.pyplot as plt
import os


filepath = os.getcwd()


def plot_returns(return_value):
    plt.figure()
    plt.plot(return_value)
    plt.savefig(filepath + '/returns_graph.png')
