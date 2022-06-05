from rabbitmq.connector import Connector

class UrlQueue(Connector):
    def __init__(self):
        super().__init__()

    # Url related implementation
    def setupUrlQueue(self):
        # Declare Queue
        e = self.channel.exchange_declare(exchange='urls', exchange_type='fanout')
        q = self.channel.queue_declare(queue='')
        self.channel.queue_bind(exchange='urls', queue=q.method.queue)

    def publishUrl(self, url):
        self.channel.basic_publish(exchange='urls', routing_key='', body=url)
