#!/usr/bin/env python

import pika
import json
import logging

logging.basicConfig(filename='/var/log/app/consumer.log', level=logging.DEBUG)


def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        data = json.loads(body)  # decode JSON string into a python dict
        msg = f' [x] Received: {data} type {type(data)}'
        print(msg)
        logging.info(msg)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    msg = ' [*] Waiting for messages. To exit press CTRL+C'
    print(msg)
    logging.info(msg)

    # Infinite loop
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('\nExiting...')
        logging.info('Exiting consumer')

if __name__ == '__main__':
    consumer()
