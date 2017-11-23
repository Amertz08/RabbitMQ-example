#!/usr/bin/env python

import arrow
import click
import sys

from bson.son import SON
from pymongo import MongoClient

client = MongoClient('db')
db = client.test_db


@click.group()
def cli():
    pass


@cli.command(help='Lists devices and last seen time')
def list():
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


@cli.command(help='Send stop command to device')
@click.argument('device_id')
def stop(device_id):
    device_list = db.bot_logs.distinct('device_id')

    n = len(device_id)
    target_ids = []
    for dev in device_list:
        if dev[:n] == device_id:
            target_ids.append(dev)

    if not target_ids:
        print(f'Device: "{device_id}" not found')
        print('use "bots list" to print list of devices')
        sys.exit()

    if len(target_ids) > 1:
        print(f'Multiple targets found for "{device_id}" be more specific')
        for dev_id in target_ids:
            print(f'device_id: {dev_id}')
        sys.exit()

    target_id = target_ids.pop()
    print(f'Stop command sent to: {target_id}')


if __name__ == '__main__':
    cli()
