#!/bin/sh
REPOSITORY="/mnt/Backups"
NOW=$(date +"%m-%d-%Y")
FILE=$(find /home/adamschoonover/Dropbox/Logs/ -iname borg*)
EMAIL='adam@elchert.net'
lastBorgBackup=$(borg list /mnt/Backups/ | awk '{print $1;}' | tail -n 1)
resetLog=$(echo "" > $FILE)

$resetLog

# Backup all of /home and /var/www except a few
# excluded directories
borg create -v --stats                          \
    $REPOSITORY::`hostname`-`date +%Y-%m-%d`    \
    /mnt/NAS

borg info /mnt/Backups::$lastBorgBackup >> $FILE

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. --prefix `hostname`- is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.

echo "" >> $FILE

borg prune --stats -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 --keep-monthly=6 >> $FILE

###########
# Email Log
###########

cat $FILE | mail -s "Borg Backup - $NOW" $EMAIL
printf "\n ##### EMAILED $NOW - $EMAIL ######\n" >> $FILE


borg create -p -v --stats \
--exclude "/mnt/*" --exclude "/dev/*" --exclude "/sys/*" --exclude "/proc/*" \
/mnt/ImageBackups/repo::`hostname`-`date +%Y-%m-%d` /
\

echo "slash back is done" | mail -s "done" adam@elchert.net

borg prune --stats -v /mnt/ImageBackups/repo --prefix `hostname`- \
	--keep-daily=7 --keep-weekly=4 --keep-monthly=6 >> $FILE

echo "" >> $FILE
echo "Finished root backup. $(date)" >> $FILE
