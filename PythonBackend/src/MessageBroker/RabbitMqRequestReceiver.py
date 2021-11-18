import pika
from MessageBroker import ActiveConnecitons
from MessageBroker import RabbitMqResponder


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
        rmq_resp = RabbitMqResponder.RabbitMqResponder()
        location = "C:\\Dev\\University\\COM624_Assignment\\PythonBackend\\Stock_Data\\rolling_graph_AAPL.png"
        rmq_resp.respond_with_prediction(location)
