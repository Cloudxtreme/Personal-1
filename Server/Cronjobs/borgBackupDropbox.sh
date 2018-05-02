#!/bin/sh

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

REPOSITORY="/mnt/Backups/DropBoxBackup/"

LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"
lastBorgBackup=$(sudo borg list /mnt/Backups/DropBoxBackup/ | awk '{print $1;}' | tail -n 1)

# Backup all of /home and /var/www except a few
# excluded directories
sudo borg create -v --stats $REPOSITORY::`hostname`-`date +%Y-%m-%d` /home/aelchert/Dropbox/

if [ $? -eq 0 ]; then
  echo -e "++ [borgBackupDropbox.sh] - $LOGDATE - Completed" >> $LOGFILE

borg prune --stats -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 >> $LOGFILE

if [ $? -eq 0 ]; then
  echo -e "++ [borgBackupDropbox.sh] - $LOGDATE - Prune - Completed" >> $LOGFILE
else
  echo -e "-- [borgBackupDropbox.sh] - $LOGDATE - Prune - FAILED" >> $LOGFILE
fi
