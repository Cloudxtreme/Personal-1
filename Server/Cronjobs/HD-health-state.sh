

# Script to check btrfs raid status.
# Also runs ~/HDSentinel. A free HD check
# http://www.hdsentinel.com/hard_disk_sentinel_linux.php

logPath="/home/adamschoonover/Dropbox/Logs/HD-health-state.txt"
hdState=$(cat $logPath | grep "Health" | tail -n 6 | awk '{print $3;}' | grep -v -i unknown)
counter=0
email="7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com"

printf "BTRFS Check:\n\n" > $logPath

# Have to have sudo..even though run as root
sudo btrfs device stats /mnt >> $logPath

printf "\nHDSentienel:\n\n" >> $logPath

HDSentinel >> $logPath

for i in $hdState; do
	if [ $i != 100 ]; then
		cat $logPath | mail -s "HD Raid Status" $email
	else
		pass
	fi
done

if [ $counter -gt 0 ]; then
	printf "\nNo Email Needed\n\n" >> $logPath
fi
