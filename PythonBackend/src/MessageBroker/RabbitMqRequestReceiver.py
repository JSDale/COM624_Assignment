import json

import pika

import main
from MessageBroker import ActiveConnecitons, StockMessageDao, RabbitMqResponder
from MessageHandlers import RequestDao


class RabbitMqRequestReceiver:

    __broker = 'localhost'
    __queue = 'StockExchange'
    __routing_key = 'StockExchange'
    __channel = None

    def initialize_request_receiver(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__broker))
        ActiveConnecitons.active_connections.append(connection)
        self.__channel = connection.channel()
        self.__channel.queue_declare(queue=self.__queue)
        self.__channel.basic_consume(queue=self.__queue, auto_ack=True, on_message_callback=self.__callback)
        print('waiting for messages.\nPress ctrl + c to exit, which may take a few seconds')
        self.__channel.start_consuming()

    def __callback(self, ch, method, properties, message):
        print(f'received {message}')
        data = json.loads(message)
        message = RequestDao.RequestDao(**data)
        try:
            main.prediction_testing(message.Ticker, message.Source)
        except Exception as e:
            stock_message = StockMessageDao.StockMessageDao("location", [f'Error: {e}'])
            json_message = stock_message.toJSON()

            rmq_resp = RabbitMqResponder.RabbitMqResponder()
            rmq_resp.respond_with_prediction(json_message)
