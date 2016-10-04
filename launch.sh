#!/bin/sh

docker run \
-p 30001:6379 \
--net my-redis-cluster \
--name test_redis \
-d redis redis-server \
--appendonly yes
