#! /bin/bash

# This script will backup .bashrc,.ssh,.sabnzbd,.couchpotato,/home/adamschoonover/Git/my-sickbeard-install
# It copies the whole source folder to the destination folder
# tar's them and deletes the folders
#
# V. 0.1 Changed save destination to NAS Archive

NOW=$(date +"%m-%d-%Y")
HOME="/home/adamschoonover"
TMP="/tmp/UsenetBackup"

mkdir $TMP
chown adamschoonover $TMP

cp -r $HOME/.ssh/ $TMP/ssh/

cp -r $HOME/.bashrc $TMP/bashrc_backup.txt

cp -r $HOME/.sabnzbd/ $TMP/sabnzbd/

cp -r $HOME/.couchpotato/ $TMP/couchpotato/

cp -r /opt/NzbDrone/ $TMP/NzbDrone/

cd /mnt/NAS/Archive/Usenet\ Programs/

tar rf Usenet_backups.tar \
$TMP/ssh/ \
$TMP/bashrc_backup.txt \
$TMP/sabnzbd/ \
$TMP/couchpotato/ \
$TMP/NzbDrone/

chown adamschoonover cd /mnt/NAS/Archive/Usenet\ Programs/Usenet_backups.tar

rm -r $TMP
