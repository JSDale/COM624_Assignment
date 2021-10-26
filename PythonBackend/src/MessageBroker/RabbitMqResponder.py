import pika

from MessageBroker import ActiveConnecitons


class RabbitMqResponder:

    __broker = 'localhost'
    __queue = 'StockExchange'
    __routing_key = 'predictions'
    __channel = None

    def __init__(self):
        self.__initialize_responder()

    def __initialize_responder(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__broker))
        ActiveConnecitons.active_connections.append(connection)
        self.__channel = connection.channel()
        self.__channel.queue_declare(queue=self.__queue)

    def respond_with_prediction(self, message):
        self.__channel.basic_publish(exchange='', routing_key=self.__routing_key, body=message)
        print(f'sent {message}')
