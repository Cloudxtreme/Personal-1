#! /bin/bash

# Script to Backup mysql database "booksread"

NOW=$(date +"%m-%d-%Y")
LOGDATE=$(date +"%m-%d-%Y %H:%M:%S")

DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

# dump Booksread database to Dropbox/Backup
mysqldump -u root -p'CuIeyy7j!!' Booksread > $DIR/booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] - $LOGDATE Completed" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] - $LOGDATE - FAILED" >> $LOGFILE
fi

# change owner of .sql backup file
chown aelchert $DIR/booksread_$NOW.sql

#adds sql backups to tar file
cd $DIR
tar rvf Booksread_Backup.tar booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] - $LOGDATE - Tar creation - Completed" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] - $LOGDATE - Tar FAILED " >> $LOGFILE
fi

chown aelchert $DIR/Booksread_Backup.tar

echo -e "Remove file"
rm *.sql