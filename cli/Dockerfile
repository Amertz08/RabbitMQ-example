FROM python:3.6

ENV PYTHONUNBUFFERED=1
RUN pip install \
    arrow==0.10.0 \
    pika==0.11.0 \
    pymongo==3.5.1
ADD . /usr/src/bots
WORKDIR /usr/src/bots

RUN pip install .

WORKDIR /home

CMD bots
