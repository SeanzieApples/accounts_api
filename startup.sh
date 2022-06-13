#!/bin/bash

set -e

if ! command -v pip3.10 &> /dev/null
then
    echo "pip3.10 could not be found, please install pip3 before continuing"
    exit
fi

if ! command -v python3.10 &> /dev/null
then
    echo "python3.10 could not be found, please install python3.10 before continuing"
    exit
fi

pip3.10 install -r requirements.txt
uvicorn app.main:app --port 8080