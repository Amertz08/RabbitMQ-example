#!/usr/bin/env python

import pika
import json


def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        data = json.loads(body)  # decode JSON string into a python dict
        print(f' [x] Received: {data} type {type(data)}')

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    # Infinite loop
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == '__main__':
    consumer()
