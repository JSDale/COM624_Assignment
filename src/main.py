import sys
import os

from StockPredicting import PandasStockPredictor as psp
from MessageBroker import MqttInitializer as mi
from MessageBroker import ActiveConnecitons


def main():
    print('hello world')


if __name__ == "__main__":
    try:
        # psp.render_rolling_average_to_graph()
        mi.initialize()
    except KeyboardInterrupt:
        ActiveConnecitons.close_connections()
        sys.exit(0)
    except SystemExit:
        ActiveConnecitons.close_connections()
