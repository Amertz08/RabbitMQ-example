FROM python:3.6

RUN pip install pika
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install .

CMD /bin/bash
