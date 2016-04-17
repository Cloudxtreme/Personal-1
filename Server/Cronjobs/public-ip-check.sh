#! /bin/bash
# Get's the public IP and writes it /Dropbox/Logs/

NOW=$(date +"%m-%d-%Y")

IP=$(curl 'http://myexternalip.com/raw')

echo $NOW "==>" $IP >> /home/adamschoonover/Dropbox/Logs/server_public_ip.txt
