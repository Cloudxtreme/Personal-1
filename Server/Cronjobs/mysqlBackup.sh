#! /bin/bash

# Script to Backup mysql database "booksread"

NOW=$(date +"%m-%d-%Y")
DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

# dump Booksread database to Dropbox/Backup
mysqldump -u root -p'CuIeyy7j!!' Booksread > $DIR/booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo "++ [mysqlBackup.sh] Completed $NOW" >> $LOGFILE
else
  echo "-- [mysqlBackup.sh] FAILED $NOW" >> $LOGFILE

# change owner of .sql backup file
chown aelchert $DIR/booksread_$NOW.sql

#adds sql backups to tar file
cd $DIR
tar rvf Booksread_Backup.tar booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo "++ [mysqlBackup.sh] Tar creation - Completed $NOW" >> $LOGFILE
else
  echo "-- [mysqlBackup.sh] Tar FAILED $NOW" >> $LOGFILE

rm booksread_$NOW.sql
# Log
