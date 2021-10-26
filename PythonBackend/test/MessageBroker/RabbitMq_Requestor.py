import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='StockExchange')

for i in range(0, 100):
    channel.basic_publish(exchange='', routing_key='StockExchange', body=str(i))
    print(f" [x] Sent {i}")
    time.sleep(1)

connection.close()
