FROM ubuntu:jammy

# Setup Crawler
COPY ./crawler-scheduler /app/crawler-scheduler
COPY ./rabbitmq /app/rabbitmq
WORKDIR /app

# Setup Python3
RUN apt-get update && apt-get install -y python3 python3-pip cron

# Setup Requirements
RUN pip3 install -r ./crawler-scheduler/requirements.txt

CMD [ "python3", "crawler-scheduler/src/UrlScrapper.py" ]
