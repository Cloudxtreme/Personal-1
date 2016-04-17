#! /bin/bash

# Script to check btrfs raid status.
# Also runs ~/HDSentinel. A free HD check
# http://www.hdsentinel.com/hard_disk_sentinel_linux.php

LogsPath="/home/adamschoonover/Dropbox/Logs"

echo "BTRFS Check:" > $LogsPath/HD-health-state.txt
echo "" 

sudo btrfs device stats /mnt >> $LogsPath/HD-health-state.txt

echo "" >> $LogsPath/HD-health-state.txt
echo "HDSentienel: " >> $LogsPath/HD-health-state.txt
echo "" >> $LogsPath/HD-health-state.txt

/home/adamschoonover/HDSentinel/HDSentinel >> $LogsPath/HD-health-state.txt
chown adamschoonover $LogsPath/HD-health-state.txt
