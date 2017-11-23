FROM python:3.6

ENV PYTHONUNBUFFERED=1
RUN pip install \
    arrow==0.10.0 \
    click==6.7.0 \
    pymongo==3.5.1
ADD . /usr/src/dbcli
WORKDIR /usr/src/dbcli

RUN pip install .

WORKDIR /home

CMD /bin/bash
