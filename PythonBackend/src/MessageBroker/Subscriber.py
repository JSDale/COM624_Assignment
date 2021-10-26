from paho.mqtt import client as mqtt_client
from MessageBroker import MqttInitializer


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f'Received: {msg.payload.decode()} from {msg.topic} topic')

    client.subscribe(MqttInitializer.topic)
    client.on_message = on_message
