#!/usr/bin/env python

import pika
import json

connection = None
channel = None
TYPES = ['producer', 'consumer']


def producer():
    global connection, channel
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
    print(f' [x] Sent {data}')
    connection.close()

if __name__ == '__main__':
    producer()
