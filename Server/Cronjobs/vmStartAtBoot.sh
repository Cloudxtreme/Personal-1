#!/bin/bash

logFile='/home/aelchert/Dropbox/Logs/cronLog.txt'

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

for vm in $(vboxmanage list vms| cut -d '"' -f 2); do
    VBoxManage startvm $vm --type headless
    if [[ $? -eq  0 ]]; then
        echo "++ [vmStartScript] - $LOGDATE - $vm - has started" >> $logFile
    elif [[ $? -eq 1 ]]; then
        echo "-- [vmStartScript] - $LOGDATE  - $vm - is already running" >> $logFile
    else
        echo "-- [vmStartScript] - $LOGDATE  - $vm - Error Occured" &>1 $logFile
     fi
done
