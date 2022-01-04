import math
import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing, model_selection
from FileManipulation import SavingToFiles
from MessageBroker import StockMessageDao
from StockPredicting import LinearRegressionModel as Lr
from StockPredicting import PolynomialRegressionSecondDegree as Pr2
from StockPredicting import PolynomialThirdDegree as Pr3
from StockPredicting import KNearestNeighbour as Knn


class PredictingTheMarket:

    __start_date = datetime.datetime(2020, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']
    __save_to_files = SavingToFiles.SaveToFiles()
    __formatted_dataframe = None
    __ticker = None
    __model_type = None
    __filepath = None
    __rmq_resp = None

    def __init__(self, filepath, rabbit_mq_responder):
        self.__filepath = filepath
        self.__rmq_resp = rabbit_mq_responder

    def get_stock_dataframe(self, ticker, source, model_type):
        print('getting data...')
        self.__model_type = model_type
        self.__ticker = ticker
        dataframe = web.DataReader(self.__ticker, source, start=self.__start_date, end=self.__end_date)
        return dataframe

    def __get_dfreg(self, dataframe):
        print(dataframe)
        self.__formatted_dataframe = dataframe.loc[:, ['Adj Close', 'Volume']]
        print(self.__formatted_dataframe)

    def predict(self, dataframe):
        self.__get_dfreg(dataframe)
        x, forecast_out = self.preprocess_x()
        x, x_lately = PredictingTheMarket.__get_x_and_y_values(x, forecast_out)
        y = self.__get_y_(forecast_out)

        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
        model = self.__select_model(x_train, y_train)

        confidence = self.__confidence_of_model(model, x_test, y_test)

        next_unix = self.get_next_unix_date()
        forecast_set = self.forecast(x_lately, model, confidence, forecast_out)
        for i in forecast_set:
            next_date = next_unix
            next_unix += datetime.timedelta(days=1)
            self.__formatted_dataframe.loc[next_date] = [np.nan for _ in range(len(self.__formatted_dataframe.columns)
                                                                               - 1)] + [i]

        title = self.__generate_title()
        self.plot_graph(title)
        file_location = f'{self.__filepath}\\{title}'
        self.__send_message_over_rabbit_mq(file_location, str(confidence))

    def __confidence_of_model(self, model, x_test, y_test):
        return model.score(x_test, y_test)

    def __generate_title(self):
        title = f'{self.__model_type}-{self.__ticker}-{datetime.datetime.now()}'
        title = title.replace(' ', '_')
        title = title.replace(':', '-')
        return title

    def __send_message_over_rabbit_mq(self, file_location, predictions):
        location = f'{file_location}.png'
        stock_message = StockMessageDao.StockMessageDao(location, predictions)
        json = stock_message.toJSON()
        self.__rmq_resp.respond_with_prediction(json)

    @staticmethod
    def __get_x_and_y_values(x, forecast_out):
        # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
        x_lately = x[-forecast_out:]
        x = x[:-forecast_out]
        print('Dimension of X', x.shape)
        return x, x_lately

    def __get_y_(self, forecast_out):
        # Separate label and identify it as y
        y = np.array(self.__formatted_dataframe['label'])
        y = y[:-forecast_out]
        print('Dimension of y', y.shape)
        return y

    def forecast(self, x_lately, model, confidence, forecast_out):
        forecast_set = model.predict(x_lately)
        self.__formatted_dataframe['Forecast'] = np.nan
        print(forecast_set, confidence, forecast_out)
        return forecast_set

    def preprocess_x(self):
        forecast_out = self.__format_data()
        x = self.__extract_value_of_x(forecast_out)
        # Scale the X so that everyone can have the same distribution for linear regression
        x = preprocessing.scale(x)
        return x, forecast_out

    def get_next_unix_date(self):
        last_date = self.__formatted_dataframe.iloc[-1].name
        last_unix = last_date
        next_unix = last_unix + datetime.timedelta(days=1)
        return next_unix

    def plot_graph(self, title):
        plt.clf()
        save_to_files = SavingToFiles.SaveToFiles()
        save_to_files.save_graph_as_png(title, self.__filepath)
        self.__formatted_dataframe['Adj Close'].tail(500).plot()
        self.__formatted_dataframe['Forecast'].tail(500).plot()
        plt.legend(loc=4)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(title)
        save_to_files.save_graph_as_png(title, self.__filepath)

    def __select_model(self, x_train, y_train):
        if self.__model_type.lower() == 'linear regression':
            return Lr.LinearRegressionModel.apply_linear_regression(x_train, y_train)
        elif self.__model_type.lower() == 'polynomial regression 2d':
            return Pr2.PolynomialRegressionSecondDegree.apply_quadratic_regression_second_degree(x_train, y_train)
        elif self.__model_type.lower() == 'polynomial regression 3d':
            return Pr3.PolynomialThirdDegree.apply_quadratic_regression_third_degree(x_train, y_train)
        elif self.__model_type.lower() == 'k nearest neighbour':
            return Knn.KNearestNeighbour.apply_k_nearest_neighbour(x_train, y_train)

        raise Exception('The model is not correct, choose again.')

    def __extract_value_of_x(self, forecast_out):
        # Separating the label here, we want to predict the AdjClose
        forecast_col = 'Adj Close'
        self.__formatted_dataframe['label'] = self.__formatted_dataframe[forecast_col].shift(-forecast_out)
        x = np.array(self.__formatted_dataframe.drop(['label'], 1))
        return x

    def __format_data(self):
        # Drop missing value
        self.__formatted_dataframe.fillna(value=-99999, inplace=True)
        print(self.__formatted_dataframe.shape)
        # We want to separate 5 percent of the data to forecast
        forecast_out = int(math.ceil(0.05 * len(self.__formatted_dataframe)))
        return forecast_out
