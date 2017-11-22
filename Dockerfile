FROM python:3.6

ENV PYTHONUNBUFFERED=1
RUN pip install pika==0.11.0
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install .

CMD /bin/bash
