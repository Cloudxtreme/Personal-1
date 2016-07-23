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

bashrcLocation="/home/adamschoonover/.bashrc"
bashrcBackup="/home/adamschoonover/Git/Personal/Backups/Bash/server_bashrc" 

imacSSH="adamschoonover@10.0.0.10"
imacPath="/Users/adamschoonover/.bash_profile"
imacBKPath="/home/adamschoonover/Git/Personal/Backups/Bash/imac_bashprofile"
imacBashCheck=$(ssh $imacSSH $imacPath)

counter=0

git_add() {
  cd /home/adamschoonover/Git/Personal/
  git add -A .
  git commit -m "updates $NOW"
  git push
}


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
if [[ $(cmp -s $bashrcLocation $bashrcBackup) == 1 ]]; then
	cp $bashrcLocation $bashrcBackup
	printf "\n Updated Bashrc backup - $NOW\n" >> $dbDirectory/systemconf_backups.txt
   counter+=1
fi

# Grab a copy of iMac bash profile
#if [[ $(cmp -s $imacBashcheck $imacBKPath) == 1 ]]; then
#	ssh $imacSSH; cp $imacPath /Users/adamschoonover/Downloads; scp $imacSSH:/Users/adamschoonover/Downloads/.bash_profile $imacBKPath
#	printf "\n Updated iMac Bash Profile - $NOW\n" >> $dbDirectory/sysemconf_backups.txt
#	counter+=1
#fi


######
# If anything is updated, push it to GIT
#####

if [[ $counter -ge 1 ]]; then
	git_add
else
	echo "No updates"
fi

# imac bashprofile


