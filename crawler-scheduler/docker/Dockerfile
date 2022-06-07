FROM python:slim

# Setup Crawler
COPY ./crawler-scheduler /app/crawler-scheduler
COPY ./rabbitmq /app/rabbitmq
WORKDIR /app

# Setup Python3
RUN pip install -r ./crawler-scheduler/requirements.txt

CMD [ "python3", "crawler-scheduler/src/UrlScrapper.py" ]
