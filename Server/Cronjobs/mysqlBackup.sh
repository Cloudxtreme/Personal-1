#! /bin/bash

# Script to Backup mysql database "booksread"

source '../../Resources/timeVariableNOW.sh'

dateLog = $(date)
DIR="/home/aelchert/Dropbox/Backup"
LOGFILE="/home/aelchert/Dropbox/Logs/cronLog.txt"

# dump Booksread database to Dropbox/Backup
mysqldump -u root -p'CuIeyy7j!!' Booksread > $DIR/booksread_$LOGFILEDATE.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] - $LOGFILEDATE Completed" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] - $LOGFILEDATE - FAILED" >> $LOGFILE
fi

# change owner of .sql backup file
chown aelchert $DIR/booksread_$NOW.sql

#adds sql backups to tar file
cd $DIR
tar rvf Booksread_Backup.tar booksread_$NOW.sql

if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] - $LOGFILEDATE - Tar creation - Completed" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] - $LOGFILEDATE - Tar FAILED " >> $LOGFILE
fi

rm booksread_$LOGFILEDATE.sql
if [ $? -eq 0 ]; then
  echo -e "++ [mysqlBackup.sh] - $LOGFILEDATE - rm of Booksread.sql - Completed" >> $LOGFILE
else
  echo -e "-- [mysqlBackup.sh] - $LOGFILEDATE - rm of Booksread.sql - FAILED " >> $LOGFILE
fi
