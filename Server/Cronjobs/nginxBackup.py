import filecmp,shutil,os

endDIR="/home/aelchert/Git/Personal/Backups/Nginx"
startDIR="/tmp/nginxTempDIR"

compare = filecmp.dircmp(startDIR,endDIR)

# see if temp directory exists. If not, create it. If so, delete and recreate it
if os.path.exists(startDIR):
	shutil.rmtree(startDIR)
	os.mkdir(startDIR)
else:
	os.mkdir(startDIR)

# pulling the files to the temp dir	
os.system('scp -q aelchert@10.0.0.57:/etc/nginx/conf.d/*.conf /home/aelchert/Git/Personal/Backups/Nginx/')

# if no new files, then exit
if len(compare.left_only) == 0:
    print "No changes"
    exit()

else:

    for files in compare.left_only:
        start = startDIR + "/" + files
        end = endDIR + "/" + files
        #print "Copying file => {}".format(files)
        shutil.copyfile(start,end)

# remove temp directory
shutil.rmtree(startDIR)
