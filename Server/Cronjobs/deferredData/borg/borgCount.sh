#!/bin/bash

##############
# Script will output a count of all files borg backs up in the
# most current backup
#
# To be used in a deferred data scirpt to SevOne
#
# v.1 Initial commit
###############

backupDirectory="/mnt/Backups"
getLatestBackupDate=$(sudo borg list $backupDirectory | awk {'print $1;'} | tail -n 1)
outputBorgCount=$(sudo borg list $backupDirectory::$getLatestBackupDate | wc -l | tee  borgCount.txt)


echo "Last backup date: "
echo $getLatestBackupDate
printf "\n"

echo "File Count: "
echo $outputBorgCount

printf "\n"

if [ $? -eq 0 ]; then
  echo "File Created Successfully"
else
  echo $?
  echo "File Not Created Successfully"
fi
