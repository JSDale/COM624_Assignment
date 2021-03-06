import sys

from ExtractingCommandLineArgs import ExtractingCommandLineArgs
from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqRequestReceiver
from StockPredicting import PredictingTheMarket
from UnderstandingData import CompareCompetitors
from UnderstandingData import PandasStockPredictor


def main():
    try:
        hostname = ExtractingCommandLineArgs.get_hostname(sys.argv)
        username = ExtractingCommandLineArgs.get_username(sys.argv)
        password = ExtractingCommandLineArgs.get_password(sys.argv)
        filepath = ExtractingCommandLineArgs.get_filepath(sys.argv)
        rabbitmq = RabbitMqRequestReceiver.RabbitMqRequestReceiver(hostname, username, password, filepath)
        rabbitmq.initialize()
    except KeyboardInterrupt:
        print('closing active connections, stand by...')
        ActiveConnecitons.close_connections()
        sys.exit(0)
    except SystemExit:
        ActiveConnecitons.close_connections()
    except Exception as e:
        print(str(e))


def risk_return_plotting():
    var = CompareCompetitors.CompareCompetitors()
    tickers = ['LOCK.L', 'QQ.L', 'HLMA.L']
    var.do_stuff(tickers)


def rolling_average_plotting():
    ticker = 'AAPL'
    PandasStockPredictor.render_rolling_average_to_graph(ticker)


if __name__ == "__main__":
    main()
    # risk_return_plotting()
    # rolling_average_plotting()
    # prediction_testing()
