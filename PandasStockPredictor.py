import datetime
import pandas_datareader.data as web
import os
import PlottingOnGraph
import PlotReturnsGraph


def get_stock_data():
    start_date = datetime.datetime(2000, 8, 1)
    end_date = datetime.datetime(2021, 10, 11)
    
    df = web.DataReader("AAPL", 'yahoo', start_date, end_date)
    filepath = os.getcwd()
    # df.to_json(filepath+'/data.json')
    df.tail()

    close_px = df['Adj Close']
    rolling_mean = close_px.rolling(window=100).mean()
    # rolling_mean.to_json(filepath+'/rolling_data.json')

    PlottingOnGraph.plot_rolling_average(close_px, rolling_mean)
    rets = close_px / close_px.shift(1) - 1
    PlotReturnsGraph.plot_returns(rets)


def print_rolling_mean_last_100_windows():
    get_stock_data()
