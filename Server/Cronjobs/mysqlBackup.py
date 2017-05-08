import os, time, subprocess

# Script to Backup mysql database "booksread"
date = time.strftime("%m-%d-%y")
directory = "/home/aelchert/Dropbox/Backup"
EMAIL = '7ac1a19215fbf24b575197605f2ae1f8f5fef8ea@api.prowlapp.com'

os.popen("mysqldump -u root -p'CuIeyy7j!!' Booksread > %s/%s.sql") % (directory, date)
