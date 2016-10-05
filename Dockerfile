FROM redis:alpine
COPY conf/redis.conf /etc/redis.conf
CMD ['"redis-server', '/etc/redis.conf']
