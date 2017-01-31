import filecmp,shutil

startDIR="/Users/aschoonover/Downloads/testing/start"
endDIR="/Users/aschoonover/Downloads/testing/end"

compare = filecmp.dircmp(startDIR,endDIR)

if len(compare.left_only) == 0:
    print "No changes"

else:

    for files in compare.left_only:
        start = startDIR + "/" + files
        end = endDIR + "/" + files
        print "Copying file => {}".format(files)
        shutil.copyfile(start,end)
