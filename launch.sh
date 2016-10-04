#!/bin/sh

docker run --name test_redis -d redis redis-server --appendonly yes
