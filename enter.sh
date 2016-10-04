#!/bin/sh

docker run -it --link test_redis:redis --rm redis redis-cli -h redis -p 6379
