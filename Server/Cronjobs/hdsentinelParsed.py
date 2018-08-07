import os

removeLines = [
    'HDD Model ID',
    'HDD Serial No',
    'HDD Revision',
    'Interface',
    'Power on time',
    'Unknown  C',
    'Unknown %',
    'Temp',
    'Temperature',
    "HDD Size"
    ]

oldFileLocation = 'hds.txt'
newFileLocation = '/home/aelchert/Dropbox/Logs/hardDriveReport.txt'

# create report from HDSentienl and put in temp folder
os.system('sudo hdsentinel > hds.txt')

# parse temp file for lines not needed and write new file without them
with open(oldFileLocation, 'r') as raw:
    with open(newFileLocation, 'w') as hds:
        for line in raw:
            if not any(words in line for words in removeLines):
                hds.write(line)

os.remove(oldFileLocation)
