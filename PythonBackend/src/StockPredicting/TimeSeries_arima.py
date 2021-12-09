from datetime import datetime

import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from FileManipulation import SavingToFiles as save
import pandas_datareader.data as web


class TimeSeriesArima:

    def get_data_frame(self, ticker, source, start_date):
        dataframe = web.DataReader(ticker, source, start=start_date, end=datetime.now())
        return dataframe

    def predict(self, data_frame):
        data_frame_close = data_frame['Close']
        training_data = data_frame_close[0:int(len(data_frame_close) * 0.7)]
        test_data = data_frame_close[int(len(data_frame_close) * 0.7):]

        history = [x for x in training_data]
        model_predictions = []
        n_test_observations = len(test_data)

        for time_point in range(n_test_observations):
            # Need to find a wat to auto-generate params below.
            # 0 = moving average.
            # 1 = I (something to do with difference.
            # 4 = AR
            correlation = self.get_correlation(data_frame)
            model = ARIMA(history, order=(4, 1, int(correlation)))
            model_fit = model.fit()
            output = model_fit.forecast()
            yhat = output[0]
            model_predictions.append(yhat)
            true_test_value = test_data[time_point]
            history.append(true_test_value)

        mse_error = mean_squared_error(test_data, model_predictions)
        print('Testing Mean Squared Error is {}'.format(mse_error))

        test_set_range = data_frame_close[int(len(data_frame_close) * 0.7):].index
        plt.plot(
            test_set_range,
            model_predictions,
            color='blue',
            marker='o',
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

        save_to_files = save.SaveToFiles()
        save_to_files.save_graph_as_png('TimeSeriesTest.png')

    def get_correlation(self, data_frame):
        restcomp = data_frame['Close'].pct_change()
        correlation = restcomp.corr
        return restcomp.mean()
