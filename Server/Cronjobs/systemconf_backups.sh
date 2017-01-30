#! /bin/bash

##
# This script makes a backup of both crontabs and bash RC. Copies them to
# Git folder and then updates Git

NOW=$(date +"%m-%d-%Y")
EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'
DIR='/home/aelchert/Git/Personal/Backups'
logFile="/home/aelchert/Dropbox/Logs/systemconf_backups.txt"
dbDirectory="/home/aelchert/Dropbox/Logs"

#nginxCFG=$(md5sum /etc/nginx/conf.d/*.conf | awk '{print $1;}')
#nginxBACKUP=$(md5sum /home/aelchert/Git/Personal/Backups/Nginx/*.conf | awk '{print $1;}')

crontabBackupHash=$(md5sum $DIR/Cron/server_root_crontab | awk '{print $1;}')
crontabHash=$(crontab -u root -l | md5sum | awk '{print $1;}')

bashrcHash=$(md5sum /home/aelchert/.bashrc | awk '{print $1;}')
bashrcBackupHash=$(md5sum /home/aelchert/Git/Personal/Backups/Bash/server_bashrc | awk '{print $1;}')

counter=0
checkFileLength() {
	fileLength=$(cat $logFile | wc -l)
	if [ "$fileLength" -gt "50" ]; then
		echo "" > $logFile
		echo "#################" >> $logFile
		echo "Sys Conf Backups" >> $logfile
		echo "#################" >> $logFile
	fi
}

git_add() {
  cd /home/aelchert/Git/Personal/
  git add -A .
  git commit -m "updates $NOW"
  git push
}

#empties log file after 100 lines
checkFileLength

# # CHECK IF Nginx conf files IS BACKED UP
# if [[ $nginxCFG != $nginxBACKUP ]]; then
# 	cp /etc/nginx/conf.d/*.conf $DIR/Nginx
# 	cp /etc/nginx/nginx.conf $DIR/Nginx
#     	printf "\n Updated Nginx conf - $NOW" >> $logFile
#     	counter+=1
# fi

#checks crontab
if [[ $crontabBackupHash != $crontabHash ]]; then
	crontab -u root -l > $DIR/Cron/server_root_crontab
	printf "\n Updated Crontab conf - $NOW" >> $logFile
   counter+=1
fi

#checks if bashrc is backed up
if [[ $bashrcHash != $bashrcBackupHash ]]; then
	cp /home/aelchert/.bashrc $DIR/Bash/server_bashrc
	printf "\n Updated Bashrc - $NOW" >> $dbDirectory/systemconf_backups.txt
   	counter+=1
fi

######
# If anything is updated, push it to GIT
#####

if [[ $counter -ge 1 ]]; then
	git_add
	echo "Sysconf Backup Complete w/ Git add- $NOW"
else
	printf "\n No updates - $NOW" >> $logFile
	echo "Sysconf Backup Complete - $NOW"
fi
