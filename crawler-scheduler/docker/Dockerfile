FROM ubuntu:jammy

# Setup Python3
RUN apt-get update && apt-get install -y python3 python3-pip

# Setup Requirements
RUN pip3 install -r requirements.txt

# Setup Crawler
COPY ./crawler-scheduler ./app
COPY ./rabbitmq ./app

# Create Cron Job
# [TODO]
