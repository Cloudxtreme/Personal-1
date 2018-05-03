#! /bin/bash

# This script backs up server's:
# 	crontab
# 	bashrc
#   nginx config from VM, via python script

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

DIR='/home/aelchert/Git/Personal/Backups'
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"
#EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'

crontabBackupHash=$(md5sum $DIR/Cron/server_root_crontab | awk '{print $1;}')
crontabHash=$(crontab -u root -l | md5sum | awk '{print $1;}')

bashrcHash=$(md5sum /home/aelchert/.bashrc | awk '{print $1;}')
bashrcBackupHash=$(md5sum $DIR/Bash/server_bashrc | awk '{print $1;}')

counter=0

checkFileLength() {
	fileLength=$(cat $LOGFILE | wc -l)
	if [ $fileLength -gt 50 ]; then
		echo -e "" > $LOGFILE
		echo -e "#################\n" >> $LOGFILE
		echo -e "Sys Conf Backups\n" >> $LOGFILE
		echo -e "#################\n\n" >> $LOGFILE
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
python3 nginxBackup.py

#checks crontab
printf "\n Checking Crontab"
if [[ $crontabBackupHash != $crontabHash ]]; then
	crontab -u root -l > $DIR/Cron/server_root_crontab
	echo "++ [systemconfBackups]- $LOGDATE - Crontab Backup " >> $LOGFILE
   counter+=1
fi

#checks if bashrc is backed up
printf "\n Checking Bashrc"
if [[ $bashrcHash != $bashrcBackupHash ]]; then
	cp /home/aelchert/.bashrc $DIR/Bash/server_bashrc
	echo "++ [systemconfBackups] - $LOGDATE - Bashrc Backup" >> $LOGFILE
   	counter+=1
fi

######
# If anything is updated, push it to GIT
#####

if [[ $counter -ge 1 ]]; then
	git_add
	echo "++ [systemconfBackups] - $LOGDATE - Sysconf Backup Complete w/ Git add" >> $LOGFILE
else
	echo "++ [systemconfBackups] - $LOGDATE - No Updates" >> $LOGFILE
fi


usage() {
    echo "Usage:"
    echo "  $0 [OPTIONS]"
    echo "Options:"
    echo "  -h      : display this help message"
    echo "  -q      : decrease verbosity level (can be repeated: -qq, -qqq)"
    echo "  -v      : increase verbosity level (can be repeated: -vv, -vvv)"
    echo "  -l FILE : redirect logging to FILE instead of STDERR"
}

while getopts "hqvl:" opt; do
    case "$opt" in
       h) usage; exit 0 ;;
       q) (( verbosity = verbosity - 1 )) ;;
       v) (( verbosity = verbosity + 1 )) ;;
       l) exec 3>>$OPTARG ;;
       *) error "Invalid options: $1"; usage; exit 1 ;;
    esac
done
