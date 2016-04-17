#! /bin/bash

# This script will backup .bashrc,.ssh,.sabnzbd,.couchpotato,/home/adamschoonover/Git/my-sickbeard-install
# It copies the whole source folder to the destination folder
# tar's them and deletes the folders

NOW=$(date +"%m-%d-%Y")

sudo cp -r /home/adamschoonover/.ssh/ /mnt/NAS/Archive/Usenet\ Programs/ssh/

sudo cp -r /home/adamschoonover/.bashrc /mnt/NAS/Archive/Usenet\ Programs/bashrc_backup.txt

sudo cp -r /home/adamschoonover/.sabnzbd/ /mnt/NAS/Archive/Usenet\ Programs/sabnzbd/

sudo cp -r /home/adamschoonover/.couchpotato/ /mnt/NAS/Archive/Usenet\ Programs/couchpotato/

#sudo cp -r /home/adamschoonover/Git/my-sickbeard-install/ /mnt/NAS/Archive/Usenet\ Programs/sickbeard/

sudo cp -r /opt/NzbDrone/ /mnt/NAS/Archive/Usenet\ Programs/NzbDrone/

cd /mnt/NAS/Archive/Usenet\ Programs/

tar czf config_backups_$NOW.tar \
/mnt/NAS/Archive/Usenet\ Programs/ssh/ \
/mnt/NAS/Archive/Usenet\ Programs/bashrc_backup.txt \
/mnt/NAS/Archive/Usenet\ Programs/sabnzbd/ \
/mnt/NAS/Archive/Usenet\ Programs/couchpotato/ \
/mnt/NAS/Archive/Usenet\ Programs/NzbDrone/


sudo rm -r ./ssh/ ./bashrc_backup.txt ./sabnzbd/ ./couchpotato/ ./NzbDrone/
