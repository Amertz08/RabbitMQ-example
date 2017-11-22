FROM python:3.6

RUN mkdir /var/log/app && touch /var/log/app/consumer.log
ENV PYTHONUNBUFFERED=1
RUN pip install pika==0.11.0
ADD . /usr/src/consumer
WORKDIR /usr/src/consumer

CMD python .
