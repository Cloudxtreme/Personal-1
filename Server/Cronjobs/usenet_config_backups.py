# This script will backup couch, sab and nzbdrone settings
#
# V. 3 Convert to Python

import subprocess
import paramiko
import os
import filecmp

HOME="/home/adamschoonover"
backupDIR="/home/adamschoonover/Git/Personal/Backups/Usenet"
couch_backupDIR = backupDIR + os.sep + "CouchPotato"

def couch_check():
    remote_couchDB = os.system('ssh vagrant@10.0.0.56 ls -t /home/vagrant/Git/CouchPotatoServer/db_backup/ | head -n 1')
    local_couchDB = os.system("ls -t /home/adamschoonover/Git/Personal/Backups/Usenet/CouchPotato *.tar.gz | head -n 1 | awk '{print $8;}'")

    try:
        if remote_couchDB == local_couchDB:
            pass
        else:
            os.system('rsync vagrant@10.0.0.56:' + '/home/vagrant/Git/CouchPotatoServer/db_backup/' + remote_couchDB + " " + backupDIR + os.sep + CouchPotato)
    except:
        print "Did not work"

print couch_check()
