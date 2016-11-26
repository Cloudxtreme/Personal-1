

# Script to check btrfs raid status.
# Also runs ~/HDSentinel. A free HD check
# http://www.hdsentinel.com/hard_disk_sentinel_linux.php

LogPath="/home/adamschoonover/Dropbox/Logs/HD-health-state.txt"
hdState=$(cat $LogPath | grep "Health" | tail -n 6 | awk '{print $3;}')
counter=0
email="7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com"

printf "BTRFS Check:\n\n" > $LogPath

# Have to have sudo..even though run as root
sudo btrfs device stats /mnt >> $LogPath

printf "\nHDSentienel:\n\n" >> $LogPath

HDSentinel >> $LogPath

for i in $hdState; do
	if [ $i != 100 ]; then
		cat $LogPath | mail -s "HD Raid Status" $email
	else
		counter=$((counter+1))
	fi
done

if [ $counter -gt 0 ]; then
	printf "\nNo Email Needed\n\n" >> $LogPath
fi
