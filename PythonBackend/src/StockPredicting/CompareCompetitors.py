import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

from StockPredicting import PandasStockPredictor as psp
from FileManipulation import SavingToFiles


class CompareCompetitors:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2021, 9, 21)
    __end_date = datetime.datetime(2021, 10, 1)
    __stock_type = 'Adj Close'

    def do_stuff(self, tickers):
        dataframe = self.get_competitors_stock_data(tickers)
        restcomp = self.get_correlation(dataframe)
        self.plot_returns_rate_and_risk(restcomp)

    def get_competitors_stock_data(self, tickers):
        try:
            print('getting competitors data...')
            dataframe = web.DataReader(tickers, self.__information_source, start=self.__start_date,
                                       end=self.__end_date)[self.__stock_type]
            print('saving to file')
            # psp.save_to_json(dataframe, 'competition_stocks.json')
            return dataframe
        except Exception as e:
            print(f'error: {str(e)}')

    def get_correlation(self, dataframe):
        restcomp = dataframe.pct_change()
        correlation = restcomp.corr
        # psp.save_to_json(restcomp, 'percentage_change.json')
        print(restcomp)
        return restcomp

    def plot_returns_rate_and_risk(self, restcomp):
        plt.figure()
        plt.scatter(restcomp.mean(), restcomp.std())
        plt.xlabel('Expected returns')
        plt.ylabel('Risk')
        for label, x, y in zip(restcomp.columns, restcomp.mean(), restcomp.std()):
            plt.annotate(
                label,
                xy=(x, y), xytext=(20, -20), textcoords='offset points', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        saving_files = SavingToFiles.SaveToFiles()
        saving_files.save_graph_as_png('returns_rate_and_risk.png')
