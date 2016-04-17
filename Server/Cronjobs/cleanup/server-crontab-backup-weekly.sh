#! /bin/bash

# Script to tar weekly crontab tar's in /Dropbox/Backup

NOW=$(date +"%m-%d-%Y")

tar czf /home/adamschoonover/Dropbox/Backup/server_crontab_backup-weekly-$NOW.tar \
/home/adamschoonover/Dropbox/Backup/server_crontab_backup_*

rm /home/adamschoonover/Dropbox/Backup/server_crontab_backup_*.tar
