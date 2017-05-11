#!/bin/sh
REPOSITORY="/mnt/Backups/"
NOW=$(date +"%m-%d-%Y")
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"
EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'
lastBorgBackup=$(sudo borg list /mnt/Backups/ | awk '{print $1;}' | tail -n 1)

resetLog() {
    echo "" > $LOGFILE
}

#clear the log
resetLog

# Backup all of /home and /var/www except a few
# excluded directories
sudo borg create -v --stats $REPOSITORY::`hostname`-`date +%Y-%m-%d` /mnt/NAS

if [ $? -eq 0 ]; then
  echo "++ [borgBackup.sh] Completed $NOW" >> $LOGFILE
else
  echo "-- [borgBackup.sh] FAILED $NOW" >> $LOGFILE
fi

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. --prefix `hostname`- is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.

#echo "" >> $LOGFILE

borg prune --stats -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 >> $LOGFILE

if [ $? -eq 0 ]; then
  echo "++ [borgBackup.sh - Prune] Completed $NOW" >> $LOGFILE
else
  echo "-- [borgBackup.sh - Prune] FAILED $NOW" >> $LOGFILE
fi
