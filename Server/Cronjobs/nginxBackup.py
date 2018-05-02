#!/usr/bin/python3.6

import filecmp,shutil,os

def debugPrint(x):
    if __name__ == '__main__':
        print(x)
'''
PURPOSE: Keep a backup of active nginx conf files

1. ssh into nginx vm
2. pull nginx conf files to a local tmp directory
3. compare conf files in tmp directory to backup directory
4. copy over new files
5. delete files in tmp directory

filecmp url: https://docs.python.org/2/library/filecmp.html

v.2 - 5/2/18 - Script wasn't working. Cleaned it up and added functionality to clean it up the 
backup dir of non-used files.
'''

tmpDir="/tmp/nginxTempDIR"
backupDir="/home/aelchert/Git/Personal/Backups/Nginx/"

# See if tmp folder exists. If not, create it. 
# If it does already, delete and recreate it to start fresh

if os.path.exists(tmpDir):
    debugPrint("Folder Existed - Deleting")
    shutil.rmtree(tmpDir)
    debugPrint("Folder Created")
    os.mkdir(tmpDir)
else:
    debugPrint("Creating Directory")
    os.mkdir(tmpDir)

# Pull files from nginx 
os.system('scp -q aelchert@10.0.0.57:/etc/nginx/conf.d/* {}'.format(tmpDir))

# Compares tmp and backup directory
compare = filecmp.dircmp(tmpDir, backupDir)

# takes the comparison and tells you if the backup directory has files the tmp does not
filesToCleanUp = compare.right_only

# these are files that are in the tmp directory only
filesToBackup = compare.left_only

# Clean up backup directory of files not in current use
# compares files in tmp directory to backup dir
for file in filesToCleanUp:
    debugPrint("Files exist")
    debugPrint("Removing File: {}".format(file))
    os.remove(backupDir + file)

# if no new files, remove tmp directory and then exit
if len(compare.diff_files) == 0:
    debugPrint("No different files in tmp and backup directory")
    # No new files, so delete tmp directory
    debugPrint("Removing {}".format(tmpDir))
    shutil.rmtree(tmpDir)
    exit()
else:
    for file in filesToBackup:
        start = tmpDir + "/" + file
        end = backupDir + "/" + file
        shutil.copyfile(start, end)

        debugPrint(print("Copying file => {}".format(file)))
            

# remove temp directory
debugPrint("Removing {}".format(tmpDir))
shutil.rmtree(tmpDir)