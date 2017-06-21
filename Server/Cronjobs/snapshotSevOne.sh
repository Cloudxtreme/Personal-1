#!/bin/bash

NOW=$(date +"%m-%d-%Y")
logPath='/home/aelchert/Dropbox/Logs/cronLog.txt'

VBoxManage snapshot SevOne take SevOne-$NOW

if [ $? -eq 0 ]; then
	echo "++ [SevOneVM Snapshot] - Created $NOW" >> $logPath
elif [ $? -eq 1 ]; then
	echo "-- [SevOne VM Snapshot] - ERROR $NOW" >> $logPath
else
	echo "-- [SevOne VM Snapshot] - Unknown Error" >> $logPath
fi


