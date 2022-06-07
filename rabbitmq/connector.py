import os
from sqlite3 import connect
import pika

class Connector:
    def __init__(self):
        self.rabbitmq_host = os.environ.get('TSMC_RABBITMQ_HOST', 'localhost')
        self.rabbitmq_port = os.environ.get('TSMC_RABBITMQ_PORT', 5672)
        self.rabbitmq_user = os.environ.get('TSMC_RABBITMQ_USER', 'user')
        self.rabbitmq_password = os.environ.get('TSMC_RABBITMQ_PASSWORD', 'password')

        self.connect()

    def connect(self):
        # Connect to Host
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.rabbitmq_host,
                port=self.rabbitmq_port,
                credentials=pika.PlainCredentials(self.rabbitmq_user, self.rabbitmq_password)
            )
        )

        # Create Channel
        self.channel = self.connection.channel()
