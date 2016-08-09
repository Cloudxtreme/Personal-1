#! /bin/bash
# Get's the public IP and writes it /Dropbox/Logs/

NOW=$(date +"%m-%d-%Y")
filePath="/home/adamschoonover/Dropbox/Logs/server_public_ip.txt"
IP=$(curl 'http://myexternalip.com/raw')

getIP (){
echo $NOW "==>" $IP >> $filePath
}

# run function
getIP

ownerName=$(stat -c %U /home/adamschoonover/Git/Personal/Server/Cronjobs/public-ip-check.sh)

if [ "$ownerName" != "adamschoonover" ]; then
	chown adamschoonover $filePath | tail -n 1
else
	exit 0
fi

if [ $(cat $filePath | wc -l) > 20 ]; then
	printf "#######\n\n Public IP Address\n\n#######\n\n" > $filePath
	getIP
else
	exit 0
fi
