import datetime
import unittest
import pandas_datareader.data as web

from StockPredicting import TimeSeries_arima


class TestArima(unittest.TestCase):

    def test_can_save_graph(self):
        print('getting data...')
        dataframe = web.DataReader('QQ.L', 'yahoo', start='2020-01-01', end=datetime.datetime.now())
        arima = TimeSeries_arima.TimeSeriesArima()
        arima.predict(dataframe)

        self.assertTrue(True)

    def test_hello_world(self):
        print('hello world')
