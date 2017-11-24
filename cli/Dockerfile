FROM python:3.6

ENV PYTHONUNBUFFERED=1
ADD . /usr/src/bots
WORKDIR /usr/src/bots

RUN pip install .

WORKDIR /home

CMD bots
