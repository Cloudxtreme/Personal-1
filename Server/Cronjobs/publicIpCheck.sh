#! /bin/bash
# Get's the public IP and writes it /Dropbox/Logs/

NOW=$(date +"%m-%d-%Y")
filePath="/home/aelchert/Dropbox/Logs/server_public_ip.txt"
IP=$(curl 'http://myexternalip.com/raw')
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

getIP (){
echo -e $NOW "==>" $IP >> $filePath
}

# run function
getIP

if [ $? -eq 0 ]; then
  echo -e "++ [publicIpCheck.sh] Completed $NOW" >> $LOGFILE
else
  echo -e "-- [publicIpCheck.sh] FAILED $NOW" >> $LOGFILE
fi

# If the log file is longer than 20 lines, clear it.
if [ $(cat $filePath | wc -l) -ge 20 ]; then
	echo -e "#######\n\n Public IP Address\n\n#######\n\n" > $filePath
	getIP
else
	exit 0
fi

# check to see if owner of the file is correct
ownerName=$(stat -c %U /home/aelchert/Git/Personal/Server/Cronjobs/publicIpCheck.sh)

if [ $ownerName != "aelchert" ]; then
        chown aelchert $filePath
				echo -e "++ [publicIpCheck.sh] chown of files completed - $NOW" >> $LOGFILE
fi
