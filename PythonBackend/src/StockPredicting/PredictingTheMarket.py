import pandas_datareader.data as web
import datetime
import math
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


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

    def predict(self, percentages):
        # drop missing values
        percentages.fillna(value=99999, inplace=True)
        # separate to 1% of the data to forecast
        forecast_out = int(math.ceil(0.01 * len(percentages)))

        # Separating label here, to predict the Adjusted close.
        forecast_col = 'Adj Close'
        percentages['label'] = percentages[forecast_col].shift(-forecast_out)

        x_train = self.__train_x(percentages, forecast_out)
        y_train = self.__train_y(percentages, forecast_out)

        clfreg = LinearRegression(n_jobs=-1)
        clfreg.fit(x_train, y_train)

        clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
        clfpoly2.fit(x_train, y_train)

        clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
        clfpoly3.fit(x_train, y_train)

        confidencereg = clfreg.score(x_train, y_train)
        confidencepoly2 = clfpoly2.score(x_train, y_train)
        confidencepoly3 = clfpoly3.score(x_train, y_train)

        print(confidencereg)
        print(confidencepoly2)
        print(confidencepoly3)

    def __train_x(self, percentages, forecast_out):
        # Finally, find data series of late X and early X (train) for model generation and evaluation
        x = np.array(percentages.drop(['label'], 1))
        # X_lately = X[-forecast_out:] <-- latest x?
        x = x[:-forecast_out]
        # scale the X so that everyone can have the same distribution for linear regression
        x = preprocessing.scale(x)
        return x

    def __train_y(self, percentages, forecast_out):
        # separate and label identify as y
        y = np.array(percentages['label'])
        y = y[:-forecast_out]
        return y
