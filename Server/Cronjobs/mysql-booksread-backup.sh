#! /bin/bash

# Script to Backup mysql database "booksread"

NOW=$(date +"%m-%d-%Y")
DIR="/home/adamschoonover/Dropbox/Backup"

mysqldump -u root booksread > $DIR/booksread_$NOW.sql

chown adamschoonover $DIR/*

cd $DIR
#adds sql backups to tar file
tar rvf Booksread_Backup.tar *.sql

#Removes all original *.sql files
rm *.sql
