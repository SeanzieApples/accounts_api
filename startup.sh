#!/bin/bash

set -e

pip install -r requirements.txt
uvicorn app.main:app