#!/bin/bash

# Run BTRFS system check, returns something like
#[/dev/sdc].write_io_errs   0
#
# grep's for the 0.

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

sudo /bin/btrfs device stats /mnt/NAS/ | grep -vE ' 0$'

echo "repsonse was: "
echo $?
echo ""


# If something is returned, send email
if [[$? == 0]]; then
  echo "There was a response"
  echo -e "++ [btrfsCheck.sh] - $LOGDATE - btrfs health check - [FAILED]" >> $LOGFILE
else
  echo "No response"
  echo -e "-- [btrfsCheck.sh] - $LOGDATE - btrfs health check - [OK]" >> $LOGFILE
fi
