# Script Map
# What are these scripts?
# Updated last: 12/9/15

## ./Dropbox/Scripts/

book_input_final.py - script to add new books to mysqlbooks
book_input_update_old_entries_1.py - script to add information to old sql entries
bookstrap_home_server.sh - post ubuntu 14 install scripts
crashplan-backup-verify.sh - looks at crashplan log and pulls newest date
sickbeard.sh - script to start sickbeard
ssh-tunnel-home.sh - script to use remotely to ssh tunnel into server/imac
vnc.sh - starts vnc

## ./Dropbox/Scripts/Cronjobs

backup_nas_to_external.sh -> takes all /mnt/NAS/ files and copies them to /mnt/Backup/ 
crontab_backup.sh -> backsup both adamschoonover and root crontab entries
dropbox_backup.sh -> backsup and tar's Dropbox
mysqlbooks_backup -> tcpdump of mysql database 'booksread'
server_ip_address -> curl's the public IP address and outputs to ~/Dropbox/Logs/ipaddress.txt
usenet_programs_configs_backup.sh -> takes the whole folders of couch, sick and snzbd and tar's them for backup
