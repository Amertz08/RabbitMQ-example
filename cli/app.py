#!/usr/bin/env python

import arrow
import click

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


if __name__ == '__main__':
    cli()
