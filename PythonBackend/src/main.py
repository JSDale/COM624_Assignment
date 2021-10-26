import sys
import threading

from StockPredicting import PandasStockPredictor as psp
from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqRequestReceiver as rr



def main():
    print('hello world')


if __name__ == "__main__":
    try:
        # psp.render_rolling_average_to_graph()
        rr = rr.RabbitMqRequestReceiver()
        rr.initialize_request_receiver()
        # mi.initialize()
    except KeyboardInterrupt:
        print('closing active connections, stand by...')
        ActiveConnecitons.close_connections()
        sys.exit(0)
    except SystemExit:
        ActiveConnecitons.close_connections()
