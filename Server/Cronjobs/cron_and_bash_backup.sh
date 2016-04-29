#! /bin/bash

##
# This script makes a backup of both crontabs and bash RC. Copies them to
# Git folder and then updates Git

NOW=$(date +"%m-%d-%Y")
DIR='/home/adamschoonover/Git/Personal/Backups'


# Creates a .crontab backup in tmp directory
crontab -u root -l > $DIR/Cron/server_root_crontab
crontab -u adamschoonover -l > $DIR/Cron/server_aschoonover_crontab

cp /home/adamschoonover/.bashrc $DIR/Bash/server_bashrc

cd $DIR

sudo git add -A .
sudo git commit -m "updates $NOW"
sudo git push
