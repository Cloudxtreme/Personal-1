#! /bin/bash

# Script to Backup mysql database "booksread"

NOW=$(date +"%m-%d-%Y")
DIR="/home/aelchert/Dropbox/Backup"

# dump Booksread database to Dropbox/Backup
mysqldump -u root -p'CuIeyy7j!!' Booksread > $DIR/booksread_$NOW.sql

# change owner of .sql backup file
chown aelchert $DIR/booksread_$NOW.sql

#adds sql backups to tar file
cd $DIR
tar rvf Booksread_Backup.tar booksread_$NOW.sql
rm booksread_$NOW.sql
# Log
echo "Added booksread_$NOW to $DIR/Booksread_Backup.tar - $NOW" >> /home/aelchert/Dropbox/Logs/mysqlBackup.txt
