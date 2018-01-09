#!/bin/bash

backupDirectory="/mnt/Backups"
getLatestBackupDate=$(sudo borg list $backupDirectory | awk {'print $1;'} | tail -n 1)
outputBorgCount=$(sudo org list $backupDirectory::$getLatestBackupDate | wc -l | tee  borgCount.txt)


echo "Last backup date: "
echo $getLatestbackupDate

echo "File Count: "
echo $outputBorgCount
