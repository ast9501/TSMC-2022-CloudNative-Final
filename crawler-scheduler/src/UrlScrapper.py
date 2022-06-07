# This script serve as an example of a urls producer.
import os
import sys
import logging
from datetime import datetime
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
            'time': datetime.date(datetime.now()).strftime("%Y-%m-%d"),
            'data': [],
        }
        # Compromise: Compress Keywords
        term = " ".join(TARGET_KEYWORDS[k])

        logging.info("Searching for %s..." % term)

        for r in search(term, num_results=NUMS_OF_SEARCH_RESULT):
            if str(r).startswith(BLACKLIST):
                continue
            if r not in result['data']:
                logging.info("Retrieveing URL: %s" % r)
                result['data'].append(r)

        payload.append(result)

    # Publish the request
    urlQueue.publishUrl(payload)

    logging.info("UrlScrapper finished.")
