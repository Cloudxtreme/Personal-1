#! /bin/bash

##
# This script makes a backup of both crontabs and bash RC. Copies them to
# Git folder and then updates Git

NOW=$(date +"%m-%d-%Y")
DIR='/home/adamschoonover/Git/Personal/Backups'
logFile="/home/adamschoonover/Dropbox/Logs/config_backups.txt"
dbDirectory="/home/adamschoonover/Dropbox/Logs"

haproxyCFG=$(md5sum /etc/haproxy/haproxy.cfg | awk '{print $1;}')
haproxyBACKUP=$(md5sum /home/adamschoonover/Git/Personal/Backups/Haproxy/haproxy.cfg | awk '{print $1;}')

crontabBackupHash=$(md5sum $DIR/Cron/server_root_crontab | awk '{print $1;}')
crontabHash=$(crontab -u root -l | md5sum | awk '{print $1;}')

bashrcHash=$(md5sum /home/adamschoonover/.bashrc | awk '{print $1;}')
bashrcBackupHash=$(md5sum /home/adamschoonover/Git/Personal/Backups/Bash/server_bashrc | awk '{print $1;}')

counter=0

check_file_length(){
	fileLength=$(cat $logFile | wc -l)
	if [[$fileLength >= "50"]]; then
        	echo "" > $logFile
	fi
}

git_add() {
  cd /home/adamschoonover/Git/Personal/
  git add -A .
  git commit -m "updates $NOW"
  git push
}

check_file_length

# CHECK IF HAPROXY IS BACKED UP
if [[ $haproxyCFG != $haproxyBACKUP ]]; then
    cp /etc/haproxy/haproxy.cfg $DIR/Haproxy/
    printf "\n Updated HAPROXY conf - $NOW\n" >> $dbDirectory/systemconf_backups.txt
    counter+=1
fi

#checks crontab
if [[ $crontabBackupHash != $crontabHash ]]; then
	crontab -u root -l > $DIR/Cron/server_root_crontab
   printf "\n Updated Crontab conf - $NOW\n" >> $dbDirectory/systemconf_backups.txt
   counter+=1
fi

#checks if bashrc is backed up
if [[ $bashrcHash != $bashrcBackupHash ]]; then
	cp /home/adamschoonover/.bashrc $DIR/Bash/server_bashrc
	printf "\n Updated Bashrc - $NOW\n" >> $dbDirectory/systemconf_backups.txt
   counter+=1
fi

######
# If anything is updated, push it to GIT
#####

if [[ $counter -ge 1 ]]; then
	git_add
else
	echo "No updates"
fi
