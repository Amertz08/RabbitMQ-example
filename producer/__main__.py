#!/usr/bin/env python

import pika
import json
import logging

logging.basicConfig(filename='/var/log/app/producer.log', level=logging.DEBUG)

def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    # Currently a python dict
    data = {
        'key': 'myvalue'
    }

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=json.dumps(data))  # Encode as a JSON string
    msg = f' [x] Sent {data}'
    print(msg)
    logging.info(msg)
    connection.close()

if __name__ == '__main__':
    producer()
