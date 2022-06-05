# This script serve as an example of a urls producer.
import os
import sys

from googlesearch import search

BLACKLIST = (
    'https://www.google.',
    'https://google.',
    'https://webcache.googleusercontent.',
    'http://webcache.googleusercontent.',
    'https://policies.google.',
    'https://support.google.',
    'https://maps.google.'
)

# Create RabbitMQ Connector
if __name__ == '__main__':
    # Modify import path
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../..")
    from rabbitmq.urlQueue import UrlQueue

    # Create UrlQueue
    urlQueue = UrlQueue()
    urlQueue.setupUrlQueue()

    for r in search("TSMC", num_results=20):
        if str(r).startswith(BLACKLIST):
            continue
        urlQueue.publishUrl(r)
