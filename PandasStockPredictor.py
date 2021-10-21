import datetime
import pandas_datareader.data as web
import os
import PlottingOnGraph


def get_stock_data():
    start_date = datetime.datetime(2019, 8, 1)
    end_date = datetime.datetime(2021, 10, 11)
    
    df = web.DataReader("AAPL", 'yahoo', start_date, end_date)
    filepath = os.getcwd()
    # df.to_json(filepath+'/data.json')
    df.tail()

    close_px = df['Adj Close']
    rolling_mean = close_px.rolling(window=10).mean()
    print("df: ###########################################")
    print(df)
    print("rolling: ########################################")
    # rolling_mean.to_json(filepath+'/rolling_data.json')
    print(rolling_mean.tail())

    PlottingOnGraph.plot_rolling_average(close_px, rolling_mean)


def print_rolling_mean_last_100_windows():
    get_stock_data()
