#! /bin/bash

# Script to Backup mysql database "booksread"

NOW=$(date +"%m-%d-%Y")
DIR="/home/adamschoonover/Dropbox/Backup"
EMAIL='7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'


mysqldump -u root booksread > $DIR/booksread_$NOW.sql

chown adamschoonover $DIR/*

cd $DIR
#adds sql backups to tar file
tar rvf Booksread_Backup.tar *.sql

#Removes all original *.sql files
rm *.sql

# Prowl update
mail -s "Mysqlbackup Complete - $NOW" $EMAIL
