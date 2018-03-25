#!/bin/sh

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

REPOSITORY="/mnt/Backups/DropBoxBackup/"

LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"
lastBorgBackup=$(sudo borg list /mnt/Backups/DropBoxBackup/ | awk '{print $1;}' | tail -n 1)

# Backup all of /home and /var/www except a few
# excluded directories
sudo borg create -v --stats $REPOSITORY::`hostname`-`date +%Y-%m-%d` /home/aelchert/Dropbox/

#borgReturnValue=$?
#if borgReturnValue=0; do
#  echo "0" > borgReturnValue.txt
#elif borgReturnValue=1; do
#   echo "1" > borgReturnValue.txt
#else
#   echo "Bad return value" > borgReturnValue.txt

if [ $? -eq 0 ]; then
  echo -e "++ [borgBackupDropbox.sh] - $LOGDATE - Completed" >> $LOGFILE

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. --prefix `hostname`- is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.

#echo "" >> $LOGFILE

borg prune --stats -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 >> $LOGFILE

if [ $? -eq 0 ]; then
  echo -e "++ [borgBackup.sh] - $LOGDATE - Prune - Completed" >> $LOGFILE
else
  echo -e "-- [borgBackup.sh] - $LOGDATE - Prune - FAILED" >> $LOGFILE
fi
