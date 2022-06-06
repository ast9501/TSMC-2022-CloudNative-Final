# This script serve as an example of a urls producer.
import os
import sys
import logging
from Setting import *

from googlesearch import search

# Create RabbitMQ Connector
if __name__ == '__main__':
    # Logging Configuration
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%d-%b-%y %H:%M:%S",
        format="%(asctime)s [%(levelname)s]: %(message)s",
    )

    logging.info("Starting UrlScrapper...")

    # Modify import path
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../..")
    from rabbitmq.urlQueue import UrlQueue

    # Create UrlQueue
    urlQueue = UrlQueue()
    urlQueue.setupUrlQueue()

    payload = []
    for k in TARGET_KEYWORDS:
        # Prepare Payload
        result = {
            'type': k,
            'data': [],
        }
        for term in TARGET_KEYWORDS[k]:
            for r in search(term, num_results=20):
                if str(r).startswith(BLACKLIST):
                    continue
                logging.info("Retrieveing URL: %s" % r)
                if r not in result['data']:
                    result['data'].append(r)

        payload.append(result)

    # Publish the request
    urlQueue.publishUrl(payload)

    logging.info("UrlScrapper finished.")
