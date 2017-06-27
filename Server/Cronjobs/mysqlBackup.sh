#! /bin/bash

# Script to Backup mysql database "booksread"

source '../../Resources/timeVariableNOW.sh'

DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

# dump Booksread database to Dropbox/Backup
mysqldump -u root -p'CuIeyy7j!!' Booksread > $DIR/booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] Completed $NOW" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] FAILED $NOW" >> $LOGFILE
fi

# change owner of .sql backup file
chown aelchert $DIR/booksread_$NOW.sql

#adds sql backups to tar file
cd $DIR
tar rvf Booksread_Backup.tar booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] Tar creation - Completed $NOW" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] Tar FAILED $NOW" >> $LOGFILE
fi

rm booksread_$NOW.sql
# Log
