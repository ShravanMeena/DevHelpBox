#!/usr/bin/env bash

docker-compose down
docker-compose up -d --build --force-recreate
