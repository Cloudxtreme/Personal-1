import shutil, filecmp, os

srcFolder = "/Users/aschoonover/Git/Personal/Backups/Nginx/"
destFolder = "/Users/aschoonover/Git/Personal/Server/AnsiblePlaybooks/Roles/nginx/templates/"

# files only files that aren't update in destFolder
copyFiles = filecmp.dircmp(srcFolder,destFolder, ignore=None, hide=None).left_list
#debug #print copyFiles

for i in copyFiles:
    # Full Path variables
    srcFilePath = srcFolder + i
    destFilePath = destFolder + i

    # Copies files
    shutil.copyfile(srcFilePath, destFilePath)
    #debug print "Copying {} to {}".format(srcFilePath,destFilePath)
