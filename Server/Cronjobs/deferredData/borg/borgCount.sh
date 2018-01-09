#!/bin/bash

backupDirectory="/mnt/Backups"
getLatestBackupDate = "borg list $backupDirectory | awk {'print $1;'} | tail -n 1"
outputBorgCount="borg list $backupDirectory::$getLatestBackupDate | wc -l > borgCount.txt"
