#!/bin/sh

echo 'docker status'
docker ps
echo ''
echo 'docker logs'
docker logs test_redis
echo ''
echo 'show current configure'
python main.py 4
