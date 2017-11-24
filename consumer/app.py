#!/usr/bin/env python

import json
import logging
import pika
import pprint

from pymongo import MongoClient

logging.basicConfig(filename='/var/log/app/consumer.log', level=logging.DEBUG)

client = MongoClient('db')
db = client.test_db

QUEUE_NAME = 'device_logs'


def callback(ch, method, properties, body):
    """
    Handles consumption of messages in queue
    :param ch: Channel object consumer is listening to
    :type ch: pika.Channel
    :param method: Method object
    :type method: pika.spec.Basic.Deliver
    :param properties:
    :type properties: pika.spec.BasicProperties
    :param body: message body
    :type body: bytes
    :return:
    """

    data = json.loads(body)  # decode JSON string into a python dict
    msg = f' [x] Received: {data} type {type(data)}'
    print(msg)
    logging.info(msg)

    bot_logs = db.bot_logs
    bot_logs.insert_one(data)
    pprint.pprint(bot_logs.find_one())


def consumer():
    """Reads from queue"""

    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(callback,
                          queue=QUEUE_NAME,
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
