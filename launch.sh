#!/bin/sh

docker run \
-v /home/dunkyfool/redis:/mnt \
-p 30001:6379 \
--net my-redis-cluster \
--name test_redis \
-d redis:backup redis-server /etc/redis/conf/redis.conf #\
#--logfile /etc/redis/log/redis.log
