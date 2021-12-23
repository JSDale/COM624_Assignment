import json
import pika
from pika import PlainCredentials

from MessageBroker import ActiveConnecitons, StockMessageDao, RabbitMqResponder
from MessageHandlers import RequestDao
from StockPredicting import TimeSeries_arima
from StockPredicting.PredictingTheMarket import PredictingTheMarket


class RabbitMqRequestReceiver:

    __host = 'localhost'
    __queue = 'StockExchange'
    __username = 'guest'
    __password = 'guest'
    __routing_key = 'StockExchange'
    __channel = None
    __filepath = None

    def __init__(self, hostname, username, password, filepath):
        self.__host = hostname
        self.__username = username
        self.__password = password
        self.__filepath = filepath

    def initialize(self):
        credentials = PlainCredentials(self.__username, self.__password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.__host, credentials=credentials))
        ActiveConnecitons.active_connections.append(connection)
        self.__channel = connection.channel()
        self.__channel.queue_declare(queue=self.__queue, auto_delete=True)
        self.__channel.basic_consume(queue=self.__queue, auto_ack=True, on_message_callback=self.__callback)
        print('waiting for messages.\nPress ctrl + c to exit, which may take a few seconds')
        self.__channel.start_consuming()

    def __callback(self, ch, method, properties, message):
        print(f'received {message}')
        data = json.loads(message)
        message = RequestDao.RequestDao(**data)
        rmq_resp = RabbitMqResponder.RabbitMqResponder(self.__host)
        try:
            if message.ModelType.lower() == 'arima':
                arima = TimeSeries_arima.TimeSeriesArima(message.Ticker, self.__filepath, rmq_resp)
                dataframe = arima.get_data_frame(message.Source, '2021-01-01')
                arima.predict(dataframe)
            else:
                predicting = PredictingTheMarket(self.__filepath, rmq_resp)
                dataframe = predicting.get_stock_dataframe(message.Ticker, message.Source, message.ModelType)
                predicting.predict(dataframe)
        except Exception as e:
            stock_message = StockMessageDao.StockMessageDao("location", f'Error: {str(e)}')
            json_message = stock_message.toJSON()

            rmq_resp = RabbitMqResponder.RabbitMqResponder(self.__host)
            rmq_resp.respond_with_prediction(json_message)
