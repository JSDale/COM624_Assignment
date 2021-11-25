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
from MessageBroker import RabbitMqResponder, StockMessageDao


class PredictingTheMarket:

    __start_date = datetime.datetime(2020, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']
    __save_to_files = SavingToFiles.SaveToFiles()
    __dfreg = None

    def get_stock_dataframe(self, ticker, source):
        print('getting data...')
        dataframe = web.DataReader(ticker, source, start=self.__start_date, end=self.__end_date)
        return dataframe

    def get_dfreg(self, dataframe):
        print(dataframe)
        self.__dfreg = dataframe.loc[:, ['Adj Close', 'Volume']]
        print(self.__dfreg)

    def predict(self):
        X, forecast_out = self.preprocess_x()
        # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
        X_lately = X[-forecast_out:]
        X = X[:-forecast_out]

        # Separate label and identify it as y
        y = np.array(self.__dfreg['label'])
        y = y[:-forecast_out]

        print('Dimension of X', X.shape)
        print('Dimension of y', y.shape)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
        clfreg = self.__apply_linear_regression(X_train, y_train)
        clfpoly2 = self.__apply_quadratic_regression_two_dimensions(X_train, y_train)
        clfpoly3 = self.__apply_quadratic_regression_three_dimensional(X_train, y_train)
        clfknn = self.__apply_k_nearest_neighbour(X_train, y_train)
        confidencepoly2, predictions = self.__get_confidence_of_all_models(X_test, clfknn, clfpoly2, clfpoly3, clfreg,
                                                                           y_test)
        next_unix = self.get_next_unix_date()

        forecast_set = self.forecast(X_lately, clfpoly2, confidencepoly2, forecast_out)

        for i in forecast_set:
            next_date = next_unix
            next_unix += datetime.timedelta(days=1)
            self.__dfreg.loc[next_date] = [np.nan for _ in range(len(self.__dfreg.columns) - 1)] + [i]

        title = 'poly2_test_new'
        filepath = os.getcwd()
        file_location = f'{filepath}\\Stock_Data\\{title}.png'
        self.plot_graph(file_location, title)

        location = file_location
        stock_message = StockMessageDao.StockMessageDao(location, predictions)
        json = stock_message.toJSON()

        rmq_resp = RabbitMqResponder.RabbitMqResponder()
        rmq_resp.respond_with_prediction(json)

    def forecast(self, X_lately, clfpoly2, confidencepoly2, forecast_out):
        # Printing the forecast
        forecast_set = clfpoly2.predict(X_lately)
        self.__dfreg['Forecast'] = np.nan
        print(forecast_set, confidencepoly2, forecast_out)
        return forecast_set

    def preprocess_x(self):
        forecast_out = self.__format_data()
        X = self.__extract_value_of_x(forecast_out)
        # Scale the X so that everyone can have the same distribution for linear regression
        X = preprocessing.scale(X)
        return X, forecast_out

    def get_next_unix_date(self):
        last_date = self.__dfreg.iloc[-1].name
        last_unix = last_date
        next_unix = last_unix + datetime.timedelta(days=1)
        return next_unix

    def plot_graph(self, file_location, title):
        plt.clf()
        plt.savefig(file_location)
        self.__dfreg['Adj Close'].tail(500).plot()
        self.__dfreg['Forecast'].tail(500).plot()
        plt.legend(loc=4)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(title)
        plt.savefig(file_location)

    @staticmethod
    def __get_confidence_of_all_models(X_test, clfknn, clfpoly2, clfpoly3, clfreg, y_test):
        confidence_of_regression = clfreg.score(X_test, y_test)
        confidence_of_poly_2d = clfpoly2.score(X_test, y_test)
        confidence_of_poly_3d = clfpoly3.score(X_test, y_test)
        confidence_of_k_nearest_neighbour = clfknn.score(X_test, y_test)
        print("The linear regression confidence is ", confidence_of_regression)
        print("The quadratic regression 2 confidence is ", confidence_of_poly_2d)
        print("The quadratic regression 3 confidence is ", confidence_of_poly_3d)
        print("The knn regression confidence is ", confidence_of_k_nearest_neighbour)
        predictions = [f'confidence of linear reg: {confidence_of_regression}',
                       f'confidence of polynomial2: {confidence_of_poly_2d}',
                       f'confidence of polynomial3: {confidence_of_poly_3d}',
                       f'confidence of KNN: {confidence_of_k_nearest_neighbour}']
        return confidence_of_poly_2d, predictions

    @staticmethod
    def __apply_k_nearest_neighbour(X_train, y_train):
        clfknn = KNeighborsRegressor(n_neighbors=2)
        clfknn.fit(X_train, y_train)
        return clfknn

    @staticmethod
    def __apply_quadratic_regression_three_dimensional(X_train, y_train):
        clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
        clfpoly3.fit(X_train, y_train)
        return clfpoly3

    @staticmethod
    def __apply_quadratic_regression_two_dimensions(X_train, y_train):
        clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
        clfpoly2.fit(X_train, y_train)
        return clfpoly2

    @staticmethod
    def __apply_linear_regression(X_train, y_train):
        clfreg = LinearRegression(n_jobs=-1)
        clfreg.fit(X_train, y_train)
        return clfreg

    def __extract_value_of_x(self, forecast_out):
        # Separating the label here, we want to predict the AdjClose
        forecast_col = 'Adj Close'
        self.__dfreg['label'] = self.__dfreg[forecast_col].shift(-forecast_out)
        X = np.array(self.__dfreg.drop(['label'], 1))
        return X

    def __format_data(self):
        # Drop missing value
        self.__dfreg.fillna(value=-99999, inplace=True)
        print(self.__dfreg.shape)
        # We want to separate 5 percent of the data to forecast
        forecast_out = int(math.ceil(0.05 * len(self.__dfreg)))
        return forecast_out
