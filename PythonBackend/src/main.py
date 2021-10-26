import sys

from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqRequestReceiver
from StockPredicting import CompareCompetitors


def main():
    try:
        # psp.render_rolling_average_to_graph()

        # rabbitmq_request_receiver = RabbitMqRequestReceiver.RabbitMqRequestReceiver()
        # rabbitmq_request_receiver.initialize_request_receiver()

        compare_competition = CompareCompetitors.CompareCompetitors()
        tickers = ['AAPL', 'GOOG', 'MSFT']
        compare_competition.do_stuff(tickers)

    except KeyboardInterrupt:
        print('closing active connections, stand by...')
        ActiveConnecitons.close_connections()
        sys.exit(0)
    except SystemExit:
        ActiveConnecitons.close_connections()


if __name__ == "__main__":
    main()
