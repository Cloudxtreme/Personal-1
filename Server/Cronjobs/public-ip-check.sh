#! /bin/bash
# Get's the public IP and writes it /Dropbox/Logs/

NOW=$(date +"%m-%d-%Y")
filePath="/home/aelchert/Dropbox/Logs/server_public_ip.txt"
IP=$(curl 'http://myexternalip.com/raw')

getIP (){
echo $NOW "==>" $IP >> $filePath
}

# run function
getIP

# If the log file is longer than 20 lines, clear it. 
if [ $(cat $filePath | wc -l) -ge 20 ]; then
	printf "#######\n\n Public IP Address\n\n#######\n\n" > $filePath
	getIP
else
	exit 0
fi

# check to see if owner of the file is correct
ownerName=$(stat -c %U /home/aelchert/Git/Personal/Server/Cronjobs/public-ip-check.sh)

if [ "$ownerName" != "adamschoonover" ]; then
        chown adamschoonover $filePath
fi
