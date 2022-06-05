# This script serve as an example of a urls producer.
import os

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
class UrlProducer:
    def __init__(self):
        pass

if __name__ == '__main__':
    for r in search("TSMC", num_results=20):
        if str(r).startswith(BLACKLIST):
            continue
        print(r)
