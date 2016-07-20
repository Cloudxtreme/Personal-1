#! /bin/bash

# This script will backup couch, sab and nzbdrone settings
#
# V. 0.2 Total update

NOW=$(date +"%m-%d-%Y")
HOME="/home/adamschoonover"
backupDIR="/home/adamschoonover/Git/Personal/Backups/Usenet"
sshIP="vagrant@10.0.0.56"

git_add() {
    cd /home/adamschoonover/Git/Personal/
    git add -A .
    git commit -m "usenet backup update - $NOW"
    git push
}


### CouchPotato ###
couchpotatoDBBackupFile=$(ssh $sshIP ls -t /home/vagrant/Git/CouchPotatoServer/db_backup/ | head -n 1)
couchpotatoDBBackupDIR="/home/vagrant/Git/CouchPotatoServer/db_backup"
couchpotatoSettings="/home/vagrant/Git/CouchPotatoServer/settings.conf"

### Sabnzbd ###
sabnzbdSettings="/home/vagrant/.sabnzbd/sabnzbd.ini"

### NzbDrone ###
nzbdroneBackup=$(ssh $sshIP ls -t /home/vagrant/.config/NzbDrone/Backups/scheduled | head -n 1)
nzbdroneBackupDIR="/home/vagrant/.config/NzbDrone/Backups/scheduled"

#
scp $sshIP:$couchpotatoDBBackupDIR/$couchpotatoDBBackupFile $backupDIR/CouchPotato


#$backupDIR/NzbDrone
#$backupDIR/Sabnzbd
