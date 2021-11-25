import pika

from MessageBroker import ActiveConnecitons


class RabbitMqResponder:

    __host = 'localhost'
    __queue = 'resp_stock'
    __routing_key = 'resp_stock'
    __channel = None

    def __init__(self):
        self.__initialize_responder()

    def __initialize_responder(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__host))
        ActiveConnecitons.active_connections.append(connection)
        self.__channel = connection.channel()
        self.__channel.queue_declare(queue=self.__queue, auto_delete=True)

    def respond_with_prediction(self, message):
        self.__channel.basic_publish(exchange='', routing_key=self.__routing_key, body=message)
        print(f'sent {message}')
