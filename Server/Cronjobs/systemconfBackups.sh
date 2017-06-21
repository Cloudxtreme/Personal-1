#! /bin/bash

# This script backs up server's:
# 	crontab
# 	bashrc
#   nginx config from VM, via python script


NOW=$(date +"%m-%d-%Y")
DIR='/home/aelchert/Git/Personal/Backups'
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"
#EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'

crontabBackupHash=$(md5sum $DIR/Cron/server_root_crontab | awk '{print $1;}')
crontabHash=$(crontab -u root -l | md5sum | awk '{print $1;}')

bashrcHash=$(md5sum /home/aelchert/.bashrc | awk '{print $1;}')
bashrcBackupHash=$(md5sum $DIR/Bash/server_bashrc | awk '{print $1;}')

counter=0

checkFileLength() {
	fileLength=$(cat $logFile | wc -l)
	if [ $fileLength -gt 50 ]; then
		echo -e "" > $logFile
		echo -e "#################\n" >> $logFile
		echo -e "Sys Conf Backups\n" >> $logfile
		echo -e "#################\n\n" >> $logFile
	fi
}

git_add() {
  cd /home/aelchert/Git/Personal/
  git add -A .
  git commit -m "updates $NOW"
  git push
}

#empties log file after 100 lines
# printf "\n Checking File Length"
# checkFileLength

# run python script for nginx conf
printf "\n Running nginxBackup.py"
python nginxBackup.py

#checks crontab
printf "\n Checking Crontab"
if [[ $crontabBackupHash != $crontabHash ]]; then
	crontab -u root -l > $DIR/Cron/server_root_crontab
	echo -e "++ [systemconfBackups] - Crontab Backup - $NOW" >> $LOGFILE
   counter+=1
fi

#checks if bashrc is backed up
printf "\n Checking Bashrc"
if [[ $bashrcHash != $bashrcBackupHash ]]; then
	cp /home/aelchert/.bashrc $DIR/Bash/server_bashrc
	echo -e "++ [systemconfBackups] - Bashrc Backup - $NOW" >> $LOGFILE
   	counter+=1
fi

######
# If anything is updated, push it to GIT
#####

if [[ $counter -ge 1 ]]; then
	git_add
	printf "++ [systemconfBackups] - Sysconf Backup Complete w/ Git add- $NOW" >> $LOGFILE
else
	printf "++ [systemconfBackups] - No Updates- $NOW" >> $LOGFILE
	printf "++ [systemconfBackups] - Sysconf Backup Complete - $NOW" >> $LOGFILE
fi
