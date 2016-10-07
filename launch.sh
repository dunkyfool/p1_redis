#!/bin/sh

sudo sysctl vm.overcommit_memory=1

docker run \
-v /home/dunkyfool/redis:/data \
-p 30001:6379 \
--net my-redis-cluster \
--name test_redis \
-d redis:backup #redis-server /etc/redis/conf/redis.conf #\
#--logfile /etc/redis/log/redis.log
