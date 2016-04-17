#! /bin/bash

#rsync -rav /mnt/NAS/ /mnt/Backup/NAS/ >> ~/Dropbox/Logs/desktop_backup_sh.txt

# Rsync's recurisvely, archive, verbosely with human readable logs
rsync -ravh  /mnt/NAS/ /mnt/Backup/ > /home/adamschoonover/Dropbox/Logs/server_backup.txt
