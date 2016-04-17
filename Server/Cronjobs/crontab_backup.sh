#! /bin/bash

##
# This script makes a backup of both crontabs, moves them to
# a temp directory, tars them

NOW=$(date +"%m-%d-%Y")
DIR='/home/adamschoonover/Dropbox/Backup'
NOWDIRC='/tmp/$NOW'

# Creates a tmp directory
mkdir $NOWDIRC
chown adamschoonover $NOWDIRC

# Creates a .crontab backup in tmp directory
crontab -u root -l > $NOWDIRC/crontab_root_$NOW.crontab
crontab -u adamschoonover -l > $NOWDIRC/crontab_adamschoonover_$NOW.crontab

# Moves Crontab Backup tar to Temp
mv $DIR/Crontab_backup.tar $NOWDIRC

cd $NOWDIRC
# Adds to new .crontab files to tar
tar rvf Crontab_backup.tar *.crontab

# Deletes .crontab files
sudo rm *.crontab

# Moves the backup back to Dropbox/Backup
mv *.tar $DIR

# Changes owner
chown adamschoonover:adamschoonover $DIR/*

# Removes temp directory
rm -r $NOWDIRC
