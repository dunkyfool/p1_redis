#!/bin/sh

######################################################
#                  Global Variable                   #
######################################################
copy_name=""
latest_name=""
LOG="/data/backup.log"
DUMPFILE="/data/dump.rdb"

######################################################
#                     Function                       #
######################################################
copy() {
	copy_name="/data/dump.$(date +%Y%m%d%H%M).rdb"
	cp -v $DUMPFILE $copy_name
}

copy_check_loop() {
	while true;
	do 
		copy
		checksum=$(redis-check-rdb $copy_name|tail -n4|head -n1|cut -d' ' -f6)
		if [ "OK!" = "$checksum" ]; then
			break
		fi
	done
}

find_latest() {
	latest_name=$( ls -tl /data/dump.*.rdb|head -n1|tail -n1|rev|cut -d' ' -f1|rev)
}

######################################################
#                      Main                          #
######################################################
#echo "!dump.rdb check"
[[ ! -e $DUMPFILE ]] && echo "$(date +%Y%m%d%H%M) dump.rdb did not exist!" >> $LOG && redis-cli bgsave

#echo "!latest backup check"
find_latest
if [ "$latest_name" = "" ]; then
	echo "$(date +%Y%m%d%H%M) No backup file" >> $LOG
	copy_check_loop
fi
find_latest
echo "$(date +%Y%m%d%H%M) latest_file $latest_name" >> $LOG

#echo "!diff check"
outcome=$(diff -s $DUMPFILE $latest_name|rev|cut -d' ' -f1|rev)
if [ "$outcome" = "differ" ]; then
	echo "Find current dump.rdb is different to latest backup file!" >> $LOG
	copy_check_loop
fi
