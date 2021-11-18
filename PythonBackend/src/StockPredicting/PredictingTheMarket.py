import math
import os

import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from FileManipulation import SavingToFiles


class PredictingTheMarket:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2019, 1, 1)
    __end_date = datetime.datetime(2021, 10, 30)
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
        print(dfreg)
        return dfreg

    def predict(self, dfreg):
        # Drop missing value
        dfreg.fillna(value=-99999, inplace=True)

        print(dfreg.shape)
        # We want to separate 10 percent of the data to forecast
        forecast_out = int(math.ceil(0.1 * len(dfreg)))

        # Separating the label here, we want to predict the AdjClose
        forecast_col = 'Adj Close'
        dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
        X = np.array(dfreg.drop(['label'], 1))

        # Scale the X so that everyone can have the same distribution for linear regression
        X = preprocessing.scale(X)

        # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
        X_lately = X[-forecast_out:]
        X = X[:-forecast_out]

        # Separate label and identify it as y
        y = np.array(dfreg['label'])
        y = y[:-forecast_out]

        print('Dimension of X', X.shape)
        print('Dimension of y', y.shape)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

        # Linear regression
        clfreg = LinearRegression(n_jobs=-1)
        clfreg.fit(X_train, y_train)

        # Quadratic Regression 2
        clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
        clfpoly2.fit(X_train, y_train)

        # Quadratic Regression 3
        clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
        clfpoly3.fit(X_train, y_train)

        # KNN Regression
        clfknn = KNeighborsRegressor(n_neighbors=2)
        clfknn.fit(X_train, y_train)

        confidencereg = clfreg.score(X_test, y_test)
        confidencepoly2 = clfpoly2.score(X_test, y_test)
        confidencepoly3 = clfpoly3.score(X_test, y_test)
        confidenceknn = clfknn.score(X_test, y_test)

        print("The linear regression confidence is ", confidencereg)
        print("The quadratic regression 2 confidence is ", confidencepoly2)
        print("The quadratic regression 3 confidence is ", confidencepoly3)
        print("The knn regression confidence is ", confidenceknn)

        last_date = dfreg.iloc[-1].name
        last_unix = last_date
        next_unix = last_unix + datetime.timedelta(days=1)

        # Printing the forecast
        forecast_set = clfpoly2.predict(X_lately)
        dfreg['Forecast'] = np.nan
        print(forecast_set, confidencepoly2, forecast_out)

        for i in forecast_set:
            next_date = next_unix
            next_unix += datetime.timedelta(days=1)
            dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns) - 1)] + [i]

        dfreg['Adj Close'].tail(500).plot()
        dfreg['Forecast'].tail(500).plot()
        plt.legend(loc=4)
        plt.xlabel('Date')
        plt.ylabel('Price')
        filepath = os.getcwd()
        plt.savefig(f'{filepath}/Stock_Data/poly2_test_new.png')
