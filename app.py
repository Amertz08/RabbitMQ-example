#!/usr/bin/env python
import argparse
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


def consumer():
    global connection, channel
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='producer/consumer')
    args = parser.parse_args()

    client_type = args.type.lower()
    if client_type not in TYPES:
        print(f'{client_type} is not a valid type {TYPES}')
    elif client_type == TYPES[0]:
        producer()
    elif client_type == TYPES[1]:
        consumer()

if __name__ == '__main__':
    main()
