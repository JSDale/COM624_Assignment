import math
import os

import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing, model_selection
from FileManipulation import SavingToFiles
from MessageBroker import RabbitMqResponder, StockMessageDao
from StockPredicting import LinearRegressionModel as lrm
from StockPredicting import PolynomialRegressionTwoDimensional as pr2
from StockPredicting import PolynomialThreeDimensional as pr3
from StockPredicting import KNearestNeighbour as knn


class PredictingTheMarket:

    __start_date = datetime.datetime(2020, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']
    __save_to_files = SavingToFiles.SaveToFiles()
    __formatted_dataframe = None
    __ticker = None
    __model = None

    def get_stock_dataframe(self, ticker, source, model):
        print('getting data...')
        self.__ticker = ticker
        dataframe = web.DataReader(self.__ticker, source, start=self.__start_date, end=self.__end_date)
        return dataframe

    def __get_dfreg(self, dataframe):
        print(dataframe)
        self.__formatted_dataframe = dataframe.loc[:, ['Adj Close', 'Volume']]
        print(self.__formatted_dataframe)

    def predict(self, dataframe):
        self.__get_dfreg(dataframe)
        X, forecast_out = self.preprocess_x()
        X, X_lately = PredictingTheMarket.__get_x_and_y_values(X, forecast_out)
        y = self.__get_y_(forecast_out)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
        clfreg = lrm.LinearRegressionModel.apply_linear_regression(X_train, y_train)
        clfpoly2 = pr2.PolynomialRegressionTwoDimensional.apply_quadratic_regression_two_dimensions(X_train, y_train)
        clfpoly3 = pr3.PolynomialThreeDimensional.apply_quadratic_regression_three_dimensional(X_train, y_train)
        clfknn = knn.KNearestNeighbour.apply_k_nearest_neighbour(X_train, y_train)

        confidence_of_quadratic_two_dimensional, confidences = PredictingTheMarket.__get_confidence_of_all_models(
            X_test, clfknn, clfpoly2, clfpoly3, clfreg, y_test)

        next_unix = self.get_next_unix_date()
        forecast_set = self.forecast(X_lately, clfpoly2, confidence_of_quadratic_two_dimensional, forecast_out)
        for i in forecast_set:
            next_date = next_unix
            next_unix += datetime.timedelta(days=1)
            self.__formatted_dataframe.loc[next_date] = [np.nan for _ in range(len(self.__formatted_dataframe.columns)- 1)] + [i]

        title = self.__generate_title()
        filepath = os.getcwd()
        file_location = f'{filepath}\\Stock_Data\\{title}.png'
        self.plot_graph(file_location, title)

        PredictingTheMarket.__send_message_over_rabbit_mq(file_location, confidences)

    def __generate_title(self):
        title = f'{self.__ticker}-{datetime.datetime.now()}'
        title = title.replace(' ', '_')
        title = title.replace(':', '-')
        return title

    @staticmethod
    def __send_message_over_rabbit_mq(file_location, predictions):
        location = file_location
        stock_message = StockMessageDao.StockMessageDao(location, predictions)
        json = stock_message.toJSON()
        rmq_resp = RabbitMqResponder.RabbitMqResponder()
        rmq_resp.respond_with_prediction(json)

    @staticmethod
    def __get_x_and_y_values(X, forecast_out):
        # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
        X_lately = X[-forecast_out:]
        X = X[:-forecast_out]
        print('Dimension of X', X.shape)
        return X, X_lately

    def __get_y_(self, forecast_out):
        # Separate label and identify it as y
        y = np.array(self.__formatted_dataframe['label'])
        y = y[:-forecast_out]
        print('Dimension of y', y.shape)
        return y

    def forecast(self, X_lately, clfpoly2, confidencepoly2, forecast_out):
        # Printing the forecast
        forecast_set = clfpoly2.predict(X_lately)
        self.__formatted_dataframe['Forecast'] = np.nan
        print(forecast_set, confidencepoly2, forecast_out)
        return forecast_set

    def preprocess_x(self):
        forecast_out = self.__format_data()
        X = self.__extract_value_of_x(forecast_out)
        # Scale the X so that everyone can have the same distribution for linear regression
        X = preprocessing.scale(X)
        return X, forecast_out

    def get_next_unix_date(self):
        last_date = self.__formatted_dataframe.iloc[-1].name
        last_unix = last_date
        next_unix = last_unix + datetime.timedelta(days=1)
        return next_unix

    def plot_graph(self, file_location, title):
        plt.clf()
        plt.savefig(file_location)
        self.__formatted_dataframe['Adj Close'].tail(500).plot()
        self.__formatted_dataframe['Forecast'].tail(500).plot()
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

    def __extract_value_of_x(self, forecast_out):
        # Separating the label here, we want to predict the AdjClose
        forecast_col = 'Adj Close'
        self.__formatted_dataframe['label'] = self.__formatted_dataframe[forecast_col].shift(-forecast_out)
        X = np.array(self.__formatted_dataframe.drop(['label'], 1))
        return X

    def __format_data(self):
        # Drop missing value
        self.__formatted_dataframe.fillna(value=-99999, inplace=True)
        print(self.__formatted_dataframe.shape)
        # We want to separate 5 percent of the data to forecast
        forecast_out = int(math.ceil(0.05 * len(self.__formatted_dataframe)))
        return forecast_out