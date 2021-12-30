import matplotlib.pyplot as plt
import pandas_datareader.data as web

from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller

from FileManipulation import SavingToFiles as save
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
        save.SaveToFiles.save_to_json(dataframe, f'{self.__filepath}', f'{self.__ticker}-StockData')
        return dataframe

    def predict(self, data_frame):
        data_frame_close = data_frame['Adj Close']
        training_data = data_frame_close[0:int(len(data_frame_close) * 0.7)]
        test_data = data_frame_close[int(len(data_frame_close) * 0.7):]

        history = [x for x in training_data]
        model_predictions = []
        n_test_observations = len(test_data)
        # moving_averages = self.__calculate_moving_averages(data_frame_close)
        j = 0

        for time_point in range(n_test_observations):
            ar = 4
            i = 1
            ma = int(self.__get_correlation(data_frame))
            # ma = int(moving_averages[j])
            # if ma < 0:
            # ma = ma - (ma*2)
            # Need to find a way to auto-generate params.
            model = ARIMA(history, order=(ar, i, ma))
            model_fit = model.fit()
            output = model_fit.forecast(dynamic=False)
            yhat = output[0]
            model_predictions.append(yhat)
            true_test_value = test_data[time_point]
            history.append(true_test_value)
            j += 1

        mse_error = mean_squared_error(test_data, model_predictions)
        result = adfuller(data_frame_close)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print(f'Testing Mean Squared Error is {mse_error}')

        save_to_files = save.SaveToFiles()
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

    def __calculate_moving_averages(self, data_frame):
        arr = data_frame.array
        moving_averages = []

        for i in range(len(arr)):
            try:
                difference = int(arr[i+1]) - int(arr[i])
                moving_averages.append(difference)
                i += 1
            except:
                moving_averages.append(0)

        print('moving averages: ')
        print(moving_averages)
        return moving_averages

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
