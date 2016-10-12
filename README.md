#README
This Project is to use snapshot for backup current RedisDB.
The files, you should be interested, are
- Dockerfile
- redis.conf
- launch.sh
- backup.sh

#Dockerfile
1. Create redis.log at /etc/redis/log
2. Add redis.conf at /etc/redis/conf
3. Add backup.sh at /etc/redis

#redis.conf
1. Name logfile w/ debug level
2. RDB portion is snapshot configuration (rdbfilename:dump.rdb, dir=/data)

#launch.sh
1. Enable vm.overcommit-mermry to avoid the failure of bacjground save
2. On Docker run portion, please attach backup file to /data
>> -v /path/to/dump.rdb:/data
3. Execute backup.sh

#backup.sh
1. Every 10 sec, system compares the latest-updated backup file with current dump.rdb
2. If they are different, system backups dump.YMDHM.rdb as backup file
3. After verify by redis-check0rdb, the backup file is clean rather than corrupted data.

#Notice
Restore procedure:
1. Use redis-check-rdb to verify the backup file is healthy
2. Rename it as dump.rdb
3. Put it at the directory, you will mount to /data.
