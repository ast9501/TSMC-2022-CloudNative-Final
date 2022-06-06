FROM alpine:3.16.0

# Setup Crawler
COPY ./crawler-scheduler /app/crawler-scheduler
COPY ./rabbitmq /app/rabbitmq
WORKDIR /app

# Setup Python3
RUN apk update && apk add --no-cache python3 py3-pip && \
    pip3 install -r ./crawler-scheduler/requirements.txt

CMD [ "python3", "crawler-scheduler/src/UrlScrapper.py" ]
