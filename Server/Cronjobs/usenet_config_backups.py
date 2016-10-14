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

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect("10.0.0.56",22,username="vagrant",password='',timeout=4)
    stdin, stdout, stderr = s.exec_command('ls -t /home/vagrant/Git/CouchPotatoServer/db_backup/ | head -n 1')
    for newest_couch_backup_file in stdout.read().splitlines():
        couch_backup_file_check = backupDIR + os.sep + "CouchPotato" + os.sep + newest_couch_backup_file
        print filecmp.cmp(newest_couch_backup_file,couch_backup_file_check)

print couch_check()
