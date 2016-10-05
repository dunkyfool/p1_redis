#!/bin/sh

#version='backup'
#docker build -t redis:$version .

docker run \
-v /home/dunkyfool/Projects/p1_redis/conf:/etc/redis \
-p 30001:6379 \
--net my-redis-cluster \
--name test_redis \
-d redis redis-server /etc/redis/redis.conf
#--appendonly yes
