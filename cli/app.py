#!/usr/bin/env python

import click

from pymongo import MongoClient

client = MongoClient('db')
db = client.test_db


@click.group()
def cli():
    pass


@cli.command()
def devices():
    device_list = db.bot_logs.distinct('device_id')
    for dev in device_list:
        print(f'device_id: {dev[:10]}')


if __name__ == '__main__':
    cli()
