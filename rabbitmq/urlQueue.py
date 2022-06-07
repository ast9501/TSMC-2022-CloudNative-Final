import json

from rabbitmq.connector import Connector

class UrlQueue(Connector):
    """
    Create RabbitMQ Connector Wrapper for UrlQueue
    """

    def setupUrlQueue(self):
        """
        Setup UrlQueue with RabbitMQ AMQP protocol
        """
        # Declare Queue
        e = self.channel.exchange_declare(exchange='urls', exchange_type='fanout')
        q = self.channel.queue_declare(queue='')
        self.channel.queue_bind(exchange='urls', queue=q.method.queue)

    def publishUrl(self, payload):
        payload = json.dumps(payload)
        self.channel.basic_publish(exchange='urls', routing_key='', body=payload)

    # Callback Def
    #
    # callback(payload)
    # payload: json string
    # [
    #   {
    #       'type': 'TSMC',
    #       'time': '2018-01-01',
    #       'data': ["url"...]
    #   },
    #   {
    #       'type': 'ASML',
    #       'time': '2018-01-01',
    #       'data': ["url"...]
    #   },
    #   ...
    # ]
    def consumeUrl(self, callback):
        def callback_func(ch, method, properties, body):
            # Decode Json Payload
            payload = json.loads(body)
            callback(payload)

        self.channel.basic_consume(queue='', on_message_callback=callback_func)
        self.channel.start_consuming()
