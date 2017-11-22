FROM python:3.6

RUN mkdir /var/log/app && touch /var/log/app/producer.log
ENV PYTHONUNBUFFERED=1
RUN pip install \
    pika==0.11.0
    arrow==0.10.0
ADD . /usr/src/producer
WORKDIR /usr/src/producer

CMD python .
