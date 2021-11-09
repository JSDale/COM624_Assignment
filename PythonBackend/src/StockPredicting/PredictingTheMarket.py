import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import math
import numpy as np
import os
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from FileManipulation import SavingToFiles


class PredictingTheMarket:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2019, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']
    __save_to_files = SavingToFiles.SaveToFiles()

    def get_stock_dataframe(self, ticker):
        try:
            print('getting data...')
            dataframe = web.DataReader(ticker, self.__information_source, start=self.__start_date,
                                       end=self.__end_date)
            return dataframe
        except Exception as e:
            print(f'error: {str(e)}')

    def get_dfreg(self, dataframe):
        print(dataframe)
        dfreg = dataframe.loc[:, ['Adj Close', 'Volume']]
        dfreg['HL_PCT'] = (dataframe['High'] - dataframe['Low']) / dataframe['Close'] * 100.0
        dfreg['PCT_change'] = (dataframe['Close'] - dataframe['Open']) / dataframe['Open'] * 100.0
        print(dfreg)
        return dfreg

    def predict(self, dfreg):
        # drop missing values
        dfreg[:].fillna(0, inplace=True)
        self.__save_to_files.save_to_json(dfreg, "drfeg.json")
        print(dfreg.shape)
        amount_to_forecast = int(math.ceil(0.01 * len(dfreg)))

        # Separating label here, to predict the Adjusted close.
        forecast_col = 'Adj Close'
        dfreg['label'] = dfreg[forecast_col].shift(-amount_to_forecast)

        x = np.array(dfreg.drop(['label'], 1))
        x = preprocessing.scale(x)
        x_train = x[:-amount_to_forecast]
        x_test = x[-amount_to_forecast:]

        y = np.array(dfreg['label'])
        y_train = y[:-amount_to_forecast]
        y_test = y[-amount_to_forecast:]

        regr = LinearRegression()
        regr.fit(x_train, y_train)

        y_prediction = regr.predict(x_test)

        # The coefficients
        print("Coefficients: \n", regr.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(y_test, y_prediction))
        # The coefficient of determination: 1 is perfect prediction
        print("Coefficient of determination: %.2f" % r2_score(y_test, y_prediction))


