import random

from paho.mqtt import client as mqtt_client
from MessageBroker import Subscriber as sub

broker = 'broker.emqx.io'
port = 1883
topic = 'StockPredictions'
client_id = f'stock-predictions-{random.randint(0, 1000)}'
username = 'user'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            raise ValueError('Failed to connect, return code %d\n', rc)

        print('connected')

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def initialize():
    client = connect_mqtt()
    sub.subscribe(client)
    client.loop_forever()
