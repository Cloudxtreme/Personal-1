#!/bin/sh
REPOSITORY="/mnt/Backups"
NOW=$(date +"%m-%d-%Y")
LOGFILE=$(find /home/adamschoonover/Dropbox/Logs/ -iname borg*)
EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'
lastBorgBackup=$(borg list /mnt/Backups/ | awk '{print $1;}' | tail -n 1)

resetLog() {
    echo "" > $LOGFILE
}

#clear the log
resetLog

# Backup all of /home and /var/www except a few
# excluded directories
borg create -v --stats                          \
    $REPOSITORY::`hostname`-`date +%Y-%m-%d`    \
    /mnt/NAS

borg info /mnt/Backups::$lastBorgBackup >> $LOGFILE

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. --prefix `hostname`- is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.

echo "" >> $LOGFILE

borg prune --stats -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 --keep-monthly=3 >> $LOGFILE

###########
# Email Log
###########

echo "Borg Backup Complete - $NOW" | msmtp -t $EMAIL

printf "\n EMAILED $NOW - $EMAIL \n" >> $LOGFILE

borg create -p -v --stats \
--exclude "/mnt/*" --exclude "/dev/*" --exclude "/sys/*" --exclude "/proc/*" \
/mnt/ImageBackups/repo::`hostname`-`date +%Y-%m-%d` /
\

echo "slash back is done" | mail -s "Borg - slash backup - done" $EMAIL

borg prune --stats -v /mnt/ImageBackups/repo --prefix `hostname`- \
	--keep-daily=7 --keep-weekly=4 --keep-monthly=6 >> $LOGFILE

echo "Borg Prune Complete - $NOW" | msmtp -t $EMAIL

echo "" >> $LOGFILE
echo "Finished root backup. $(date)" >> $LOGFILE
