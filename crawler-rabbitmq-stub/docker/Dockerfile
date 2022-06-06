FROM python:slim
COPY ./crawler-rabbitmq-stub /app/crawler-rabbitmq-stub
COPY ./rabbitmq /app/rabbitmq
WORKDIR /app
RUN pip install -r crawler-rabbitmq-stub/requirements.txt
CMD ["python", "crawler-rabbitmq-stub/src/stub.py"]
