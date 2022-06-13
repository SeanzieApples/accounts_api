#!/bin/bash

docker build -t accounts_api .
docker run -it accounts_api