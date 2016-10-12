#!/bin/sh

###########################################
# Check latest 10 snapshot corrupt or not #
###########################################

files=`ls -tl /data/*.rdb|head -n5|rev|cut -d' '  -f1|rev`

for i in $files;
do
	echo -n $i
	outcome=$(redis-check-rdb $i|tail -n4|head -n1|cut -d' ' -f6)
	echo -e "\t$outcome"
done
