import yfinance as yf
import PandasStockPredictor as psp


def main():
    msft = yf.Ticker("MSFT")

    # get stock info
    # print(msft.info)

    # get historical market data
    historical_market_data = msft.history(period="5d")

    print(historical_market_data)


if __name__ == "__main__":
    psp.render_rolling_average_to_graph()
