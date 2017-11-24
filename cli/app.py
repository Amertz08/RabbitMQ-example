#!/usr/bin/env python

import arrow
import pika
import pprint
import json
import sys

from bson.son import SON
from pymongo import MongoClient

client = MongoClient('db')
db = client.test_db


def _get_target(target, devices):
    """
    Generator that returns devices that match target
    :param target: partial hash id to find
    :param devices: list of devices
    :return: list of device hashes if found
    """

    for dev in devices:
        if dev[:len(target)] == target:
            yield dev


def get_target(device_id):
    """
    Returns full hash id for given short id or None
    :param device_id: partial hash to target
    :return: device full hash id
    """

    device_list = db.bot_logs.distinct('device_id')
    target_ids = [dev for dev in _get_target(device_id, device_list)]

    if not target_ids:
        print(f'Device: "{device_id}" not found')
        print('use "ls" to print list of devices or "ll" for full ids')
        return None

    if len(target_ids) > 1:
        print(f'Multiple targets found for "{device_id}" be more specific')
        for dev_id in target_ids:
            print(f'device_id: {dev_id}')
        return None

    return target_ids.pop()


def print_bots():
    """Prints first 10 characters of device id hash"""

    device_list = db.bot_logs.aggregate([
        {'$sort': SON([('timestamp', -1)])},
        {'$group': {'_id': '$device_id', 'timestamp': {'$first': '$timestamp'}}}
    ])

    print('------------------------------------')
    print('| device_id  |      last_seen      |')
    print('------------------------------------')
    for dev in device_list:
        dev_id = dev['_id'][:10]
        last_seen = arrow.get(dev['timestamp']).format('YYYY-MM-DD HH:mm:ss')
        print(f'| {dev_id} | {last_seen} |')
    print('------------------------------------')


def print_long():
    """Prints entire device hash id"""
    device_list = db.bot_logs.aggregate([
        {'$sort': SON([('timestamp', -1)])},
        {'$group': {'_id': '$device_id', 'timestamp': {'$first': '$timestamp'}}}
    ])
    print('------------------------------------------------------------------')
    print('|                 device_id                |      last_seen      |')
    print('------------------------------------------------------------------')
    for dev in device_list:
        dev_id = dev['_id']
        last_seen = arrow.get(dev['timestamp']).format('YYYY-MM-DD HH:mm:ss')
        print(f'| {dev_id} | {last_seen} |')
    print('------------------------------------------------------------------')


def publish_cmd(device_id, cmd):
    """
    Publishes command to command queue
    :param device_id: device hash to send message to
    :param cmd: command to send
    :return: None
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()

    channel.queue_declare(queue='commands')

    data = {
        'device_id': device_id,
        'command': cmd,
        'timestamp': arrow.now().timestamp
    }
    channel.basic_publish(exchange='',
                          routing_key='',
                          body=json.dumps(data))
    pprint.pprint(data)


def print_dialog():
    """Prints command dialog"""

    print('''
    Commands:
        ls      : prints devices
        ll      : prints entire device id
        start   : moves forward
        stop    : stops bot
        use     : use device
        drop    : deselect device
        exit    : exit interactive drive
    ''')


def main():
    """Main execution for application"""

    device_id = None
    dev_short_id = None

    print_dialog()
    while True:
        try:
            comm_line = input(f'[{dev_short_id if dev_short_id else "----------"}]> ')
        except KeyboardInterrupt:
            print('\nExiting...')
            sys.exit()

        comm_vals = comm_line.split()
        if not comm_vals:
            print_dialog()
            continue

        command = comm_vals[0]
        if command == 'exit':
            print('Exiting...')
            sys.exit()
        elif command == 'start':
            if not device_id:
                print('Select a device')
                continue
            publish_cmd(device_id, command.upper())
        elif command == 'stop':
            if not device_id:
                print('Select a device')
                continue
            publish_cmd(device_id, command.upper())
        elif command == 'ls':
            print_bots()
        elif command == 'll':
            print_long()
        elif command == 'use':
            if len(comm_vals) < 2:
                print('Provide a device id')
                continue
            new_id = get_target(comm_vals[1])
            if new_id is None:
                continue
            device_id = new_id
            dev_short_id = device_id[:10]
        elif command == 'drop':
            device_id = None
            dev_short_id = None
        else:
            print_dialog()


if __name__ == '__main__':
    main()
