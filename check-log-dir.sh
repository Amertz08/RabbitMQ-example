#!/usr/bin/env bash

if [ ! -d "./logs" ]; then
    mkdir logs
else
    echo "log directory already exists"
fi
