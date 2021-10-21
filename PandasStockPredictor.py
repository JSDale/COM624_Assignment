import datetime
import pandas_datareader.data as web
import os
import PlottingOnGraph
import PlotReturnsGraph


filepath = os.getcwd()


def get_closing_stock_price(start_date, end_date, ticker):
    
    df = web.DataReader(ticker, 'yahoo', start_date, end_date)
    df.to_json(filepath+'/Data/raw_data.json')
    df.tail()
    close_px = df['Adj Close']
    return close_px


def get_moving_average(closing_stock_price):
    rolling_mean = closing_stock_price.rolling(window=100).mean()
    rolling_mean.to_json(filepath + '/Data/rolling_data.json')
    return rolling_mean


def calculate_return_value(closing_stock_price):
    returns_value = closing_stock_price / closing_stock_price.shift(1) - 1
    return returns_value


def render_rolling_average_to_graph():
    try:
        ticker = 'AAPL'
        start_date = datetime.datetime(2000, 8, 1)
        end_date = datetime.datetime(2021, 10, 11)
        closing_stock_price = get_closing_stock_price(start_date, end_date, ticker)
        moving_average = get_moving_average(closing_stock_price)
        print('data gathered and saved to json, plotting graphs...')
        PlottingOnGraph.plot_rolling_average(closing_stock_price, moving_average)
        PlotReturnsGraph.plot_returns(calculate_return_value(closing_stock_price))
        print('graphs plotted')
    except Exception as e:
        print(f"error: {e.message}")
