import sys

from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqRequestReceiver
from StockPredicting import PredictingTheMarket
from UnderstandingData import CompareCompetitors
from UnderstandingData import PandasStockPredictor


def main():
    try:
        rabbitmq_request_receiver = RabbitMqRequestReceiver.RabbitMqRequestReceiver()
        rabbitmq_request_receiver.initialize_request_receiver()

    except KeyboardInterrupt:
        print('closing active connections, stand by...')
        ActiveConnecitons.close_connections()
        sys.exit(0)
    except SystemExit:
        ActiveConnecitons.close_connections()


def prediction_testing():
    predicting = PredictingTheMarket.PredictingTheMarket()
    ticker = 'AAPL'
    dataframe = predicting.get_stock_dataframe(ticker)
    dfreg = predicting.get_dfreg(dataframe)
    predicting.predict(dfreg)


def risk_return_plotting():
    var = CompareCompetitors.CompareCompetitors()
    tickers = ['LOCK.L', 'QQ.L', 'HLMA.L']
    var.do_stuff(tickers)


def rolling_average_plotting():
    ticker = 'AAPL'
    PandasStockPredictor.render_rolling_average_to_graph(ticker)


if __name__ == "__main__":
    # main()
    # risk_return_plotting()
    # rolling_average_plotting()
    prediction_testing()
