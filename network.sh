#!/bin/sh

docker network ls
docker network create my-redis-cluster
docker network ls
