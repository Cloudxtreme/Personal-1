#! /bin/bash

# This script will backup couch, sab and nzbdrone settings
#
# V. 0.2 Total update

NOW=$(date +"%m-%d-%Y")
HOME="/home/aelchert"
backupDIR="/home/aelchert/Git/Personal/Backups/Usenet/"
sshIP="aelchert@10.0.0.55"
serverBackupDIR='/home/aelchert/Git/Personal/Backups/Usenet/'

git_add() {
    cd /home/aelchert/Git/Personal/
    git add -A .
    git commit -m "usenet backup update - $NOW"
    git push
}


### CouchPotato ###
couchpotatoDBBackupDIR='/var/opt/couchpotato'
couchpotatoDBBackupFile=$(ssh $sshIP ls -t $couchpotatoDBBackupDIR/db_backup/ | head -n 1)
couchpotatoSettings="$couchpotatoDBBackupDIR/settings.conf "

### Sabnzbd ###
sabnzbdSettings="/home/aelchert/.config/sabnzbd/sabnzbd.ini"

### NzbDrone ###
nzbdroneBackupDIR="/home/aelchert/.config/NzbDrone/Backups/scheduled"
nzbdroneBackup=$(ssh $sshIP ls -t $nzbdroneBackupDIR | head -n 1)

### Couch DB Backup
scp $sshIP:$couchpotatoDBBackupDIR/$couchpotatoDBBackupFile $backupDIR/CouchPotato
scp $sshIP:$couchpotatoSettings $backupDIR/CouchPotato

### SAB BACKUP ###
scp $sshIP:$sabnzbdSettings $backupDIR/Sabnzbd

### NzbDrone ###
scp $sshIP:$nzbdroneBackupDIR/$nzbdroneBackup $backupDIR/NzbDrone

echo "Usenet Backup Complete - $NOW"
