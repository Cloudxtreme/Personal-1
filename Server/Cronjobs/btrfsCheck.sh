#!/bin/bash

# v.2 - 5/2/18 - Fixed logging 

# Run BTRFS system check, returns something like
#[/dev/sdc].write_io_errs   0
#
# grep's for the 0.



NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

/bin/btrfs device stats /mnt/NAS/ | grep -vE ' 0$'

if [ $? -eq 0 ]; then
  echo "There was a response"
  echo -e "++ [btrfsCheck.sh] - $LOGDATE - btrfs health check - [[ FAILED ]]" >> $LOGFILE
elif [ $? -eq 1 ]; then
    echo "Health Check OK"
    echo -e "-- [btrfsCheck.sh] - $LOGDATE - btrfs health check - [[ OK ]]" >> $LOGFILE
else
  echo "Weird response"
  echo $?
  echo -e "-- [btrfsCheck.sh] - $LOGDATE - btrfs health check - [[ Weird response ]]" >> $LOGFILE
fi
