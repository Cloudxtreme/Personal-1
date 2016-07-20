#! /bin/bash

##
# This script makes a backup of both crontabs and bash RC. Copies them to
# Git folder and then updates Git

NOW=$(date +"%m-%d-%Y")
DIR='/home/adamschoonover/Git/Personal/Backups'
haproxHash=$(md5sum /etc/haproxy/haproxy.cfg | awk '{print $1;}')
gitHAProxHash=$(md5sum /home/adamschoonover/Git/Personal/Backups/Haproxy/haproxy.cfg | awk '{print $1;}')
logFile="/home/adamschoonover/Dropbox/Logs/config_backups.txt"
dbDirectory="/home/adamschoonover/Dropbox/Logs"

git_add() {

  git add -A .
  git commit -m "updates $NOW"
  git push

}


if [[ #10$haproxHash -ne #10$gitHAProxHash ]]; then
    cp /etc/haproxy/haproxy.cfg $DIR/Haproxy/

    printf "\n Updated HAPROXY conf - $NOW\n" >> $dbDirectory/systemconf_backups.txt

    git_add
fi

# Creates a .crontab backup in tmp directory
crontab -u root -l > $DIR/Cron/server_root_crontab

cp /home/adamschoonover/.bashrc $DIR/Bash/server_bashrc


## HAPROXY backup



cd $DIR
