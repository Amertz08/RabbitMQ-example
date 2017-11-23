#!/usr/bin/env python

import arrow
import hashlib
import json
import logging
import pika

logging.basicConfig(filename='/var/log/app/producer.log', level=logging.DEBUG)


def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()

    channel.queue_declare(queue='device_logs')

    # Create two unique device ids to provide more example data
    timestamp = arrow.now().timestamp
    device_name = b'A' if timestamp % 2 == 0 else b'B'
    '''
    This creates the same hash value each time so we can use the Raspberry Pi
    serial number to create a unique ID for each device
    '''
    device_id = hashlib.sha1(device_name).hexdigest()

    # Currently a python dict
    data = {
        'device_id': device_id,
        'timestamp': timestamp,
        'data': {
            'key': 'value'
        }
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
