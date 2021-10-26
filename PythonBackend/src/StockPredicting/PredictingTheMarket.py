import pandas_datareader.data as web
import datetime


class PredictingTheMarket:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2021, 9, 21)
    __end_date = datetime.datetime(2021, 10, 1)
    __stock_type = ['Adj Close']

    def get_stock_dataframe(self, ticker):
        try:
            print('getting data...')
            dataframe = web.DataReader(ticker, self.__information_source, start=self.__start_date,
                                       end=self.__end_date)
            return dataframe
        except Exception as e:
            print(f'error: {str(e)}')

    def get_percentages(self, dataframe):
        print(dataframe)
        percentages = dataframe.loc[:, ['Adj Close']]
        percentages['HL_PCT'] = (dataframe['High'] - dataframe['Low']) / dataframe['Close'] * 100.0
        percentages['PCT_change'] = (dataframe['Close'] - dataframe['Open']) / dataframe['Open'] * 100.0
        print(percentages)
        return percentages
