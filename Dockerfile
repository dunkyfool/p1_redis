FROM redis:alpine

# TRIVAL
RUN mkdir -p -m 755 /etc/redis/conf && mkdir -p -m 755 /etc/redis/log && mkdir -p -m 755 /etc/redis/run && chown -R redis:redis /etc/redis

# LOG
RUN touch /etc/redis/log/redis.log && chmod 755 /etc/redis/log/redis.log && chown redis:redis /etc/redis/log/redis.log

# CONF
ADD redis.conf /etc/redis/conf/redis.conf
RUN chmod 755 /etc/redis/conf/redis.conf && chown redis:redis /etc/redis/conf/redis.conf

# CMD
CMD ["redis-server", "/etc/redis/conf/redis.conf"]
