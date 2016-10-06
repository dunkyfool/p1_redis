#!/bin/sh

#version='backup'
#docker build -t redis:$version .

docker run \
-v /home/dunkyfool/redis/conf:/etc/redis/conf \
-v /home/dunkyfool/redis/data:/etc/redis/data \
-v /home/dunkyfool/redis/log:/etc/redis/log \
-p 30001:6379 \
--net my-redis-cluster \
--name test_redis \
-d redis redis-server /etc/redis/conf/redis.conf \
--logfile /etc/redis/log/redis.log
