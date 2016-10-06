FROM redis:alpine

# TRIVAL
RUN mkdir -p -m 755 /etc/redis/conf
RUN mkdir -p -m 755 /etc/redis/data
RUN mkdir -p -m 755 /etc/redis/log
RUN mkdir -p -m 755 /etc/redis/run
RUN chown -R redis:redis /etc/redis

# LOG
RUN touch /etc/redis/log/redis.log
RUN chmod 755 /etc/redis/log/redis.log
RUN chown redis:redis /etc/redis/log/redis.log

# CONF
ADD redis.conf /etc/redis/conf/redis.conf
RUN chmod 755 /etc/redis/conf/redis.conf
RUN chown redis:redis /etc/redis/conf/redis.conf

# CMD
CMD ["redis-server", "/etc/redis/conf/redis.conf"]
