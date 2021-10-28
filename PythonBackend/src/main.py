import sys

from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqRequestReceiver
from StockPredicting import PredictingTheMarket


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
    percentages = predicting.get_percentages(dataframe)

    # var = CompareCompetitors.CompareCompetitors()
    # tickers = ['LOCK.L', 'QQ.L']
    # var.do_stuff(tickers)


if __name__ == "__main__":
    # main()
    prediction_testing()
