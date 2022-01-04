import matplotlib.pyplot as plt
import pandas_datareader.data as web

from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller

from FileManipulation import SavingToFiles as Save
from MessageBroker.StockMessageDao import StockMessageDao


class TimeSeriesArima:

    __ticker = None
    __filepath = None
    __rmq_resp = None

    def __init__(self, ticker, filepath, rabbit_mq_responder):
        self.__ticker = ticker
        self.__filepath = filepath
        self.__rmq_resp = rabbit_mq_responder

    def __send_message_over_rabbit_mq(self, predictions, filename):
        stock_message = StockMessageDao(f'{self.__filepath}\\{filename}', predictions)
        json = stock_message.toJSON()
        self.__rmq_resp.respond_with_prediction(json)

    def get_data_frame(self, source, start_date):
        dataframe = web.DataReader(self.__ticker, source, start=start_date, end=datetime.now())
        Save.SaveToFiles.save_to_json(dataframe, f'{self.__filepath}', f'{self.__ticker}-StockData')
        return dataframe

    def predict(self, data_frame):
        data_frame_close = data_frame['Adj Close']
        training_data = data_frame_close[0:int(len(data_frame_close) * 0.7)]
        test_data = data_frame_close[int(len(data_frame_close) * 0.7):]

        history = [x for x in training_data]
        model_predictions = []
        number_test_observations = len(test_data)
        j = 0

        for time_point in range(number_test_observations):
            # number of lag observations in the model; also known as lag order.
            p = 4
            # the number of times that raw observations are differenced; also known as the degree of differencing.
            d = 1
            # the size of the moving average window; also known as the order of the moving average.
            q = int(self.__get_correlation(data_frame))
            # TODO find a way to auto-generate params.
            model = ARIMA(history, order=(p, d, q))
            model_fit = model.fit()
            output = model_fit.forecast(dynamic=False)
            y_hat = output[0]
            model_predictions.append(y_hat)
            true_test_value = test_data[time_point]
            history.append(true_test_value)
            j += 1

        mse_error = mean_squared_error(test_data, model_predictions)
        result = adfuller(data_frame_close)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print(f'Testing Mean Squared Error is {mse_error}')

        save_to_files = Save.SaveToFiles()
        plt.clf()
        title = self.__generate_title()
        save_to_files.save_graph_as_png(title, self.__filepath)

        test_set_range = data_frame_close[int(len(data_frame_close) * 0.7):].index
        plt.plot(
            test_set_range,
            model_predictions,
            color='blue',
            linestyle='dashed',
            label='Predicted Price')

        plt.plot(
            test_set_range,
            test_data,
            color='red',
            label='Actual Price')

        plt.title('Prices Prediction')
        plt.xlabel('Date')
        plt.ylabel('Prices')
        plt.legend()

        save_to_files.save_graph_as_png(title, self.__filepath)
        self.__send_message_over_rabbit_mq(mse_error, f'{title}.png')

    @staticmethod
    def __get_correlation(data_frame):
        restcomp = data_frame['Close'].pct_change()
        correlation = restcomp.corr
        return restcomp.mean()

    def __generate_title(self):
        title = f'ARIMA-{self.__ticker}-{datetime.now()}'
        title = title.replace(' ', '_')
        title = title.replace(':', '-')
        return title
