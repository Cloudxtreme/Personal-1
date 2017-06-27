#! /bin/bash
# Get's the public IP and writes it /Dropbox/Logs/

source '../../Resources/timeVariableNOW.sh'

filePath="/home/aelchert/Dropbox/Logs/server_public_ip.txt"
IP=$(curl 'http://myexternalip.com/raw')
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

getIP (){
echo -e $NOW "==>" $IP >> $filePath
}

# run function
getIP

if [ $? -eq 0 ]; then
  echo "++ [publicIpCheck.sh] - $NOW - Completed" >> $LOGFILE
else
  echo "-- [publicIpCheck.sh] - NOW - FAILED " >> $LOGFILE
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
	echo "++ [publicIpCheck.sh] - $NOW - chown of files completed" >> $LOGFILE
fi
