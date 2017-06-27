#!/bin/bash

source '../../Resources/timeVariableNOW.sh'

logPath='/home/aelchert/Dropbox/Logs/cronLog.txt'

VBoxManage snapshot SevOne take SevOne-$NOW

if [ $? -eq 0 ]; then
	echo "++ [SevOneVM Snapshot] - $NOW - Created" >> $logPath
elif [ $? -eq 1 ]; then
	echo "-- [SevOne VM Snapshot] - $NOW - ERROR" 2>&1 $logPath
else
	echo "-- [SevOne VM Snapshot] - $NOW - Unknown Error" 2>&1  $logPath
fi
