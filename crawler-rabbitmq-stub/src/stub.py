import os
import sys
import logging
import json
from requests import post

# Extract Crawler Endpoint from Environment Variable
CRAWLER_ENDPOINT = os.environ.get("TSMC_CRAWLER_ENDPOINT", "localhost")
CRAWLER_PORT = os.environ.get("TSMC_CRAWLER_PORT", "8088")

def submit_crawler(payload):
    p = {'payload': payload}
    post(f"http://{CRAWLER_ENDPOINT}:{CRAWLER_PORT}/crawler", json=p)
    logging.info(f"Payload of size {len(json.dumps(p))} submitted to crawler")

if __name__ == '__main__':
    # Logging Configuration
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%d-%b-%y %H:%M:%S",
        format="%(asctime)s [%(levelname)s]: %(message)s",
    )

    logging.info("Starting RabbitMQ Stub for Crawler...")

    # Modify import path
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../..")
    from rabbitmq.urlQueue import UrlQueue

    # Create UrlQueue
    urlQueue = UrlQueue()
    urlQueue.setupUrlQueue()

    logging.info("RabbitMQ Stub for Crawler started. [Crawler Endpoint: %s:%s]" % (CRAWLER_ENDPOINT, CRAWLER_PORT))
    logging.info("Waiting for messages...")
    urlQueue.consumeUrl(submit_crawler)
