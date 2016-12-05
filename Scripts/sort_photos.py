#!/usr/bin/env python
import exifread, datetime, os, shutil, calendar, filecmp, argparse
from blessed import Terminal
from os.path import join

#v1. A Script to take all CR2 files off the camera card
#    and move them to a folder in the Photos folder.
#    Format for destination is [year]/[num_month - name_month]/[date]
#v2. Expanded files to be moved to jpgs, fixed bugs
#v3. Added argparse
#

def date_taken_info(filename):

        open_file = open(filename, 'rb')
        tags = exifread.process_file(open_file, stop_tag='Image DateTime', details=False)

        datetaken_string = tags['Image DateTime']
        datetaken_object = datetime.datetime.strptime(datetaken_string.values, '%Y:%m:%d %H:%M:%S')

        # Creates a dict
        day = str(datetaken_object.day).zfill(2)
        month = str(datetaken_object.month).zfill(2)
        month_num = calendar.month_name[int(month)]
        year = str(datetaken_object.year)

        # Output year, month[09 - September], day[04]
        output = [year, month + " - " + month_num, day]
        return output

# take arguments
parser = argparse.ArgumentParser(
    prog="Sorting Photos",
    description="A simple script to move files from a flash drive, make the folders and move files",
)

parser.add_argument(
    "-a","--adam",
    help="Use to move images from Compact Flash to /mnt/NAS/Photos",
    dest="person",
    action="store_const",
    const="Adam"
)
parser.add_argument(
    "-s","--steven",
    help="Use to move images from SD Card to /mnt/NAS/Photos/Steven",
    dest="person",
    action="store_const",
    const="Steven"
)

args = parser.parse_args()

if args.person.lower() == "adam":
    print "add values to script"
    exit()

elif args.person.lower() == "steven":
    source_dir = "/Volumes/EOS_DIGITAL/DCIM/100CANON"
    dest_dir = "/Volumes/NAS/Photos/Steven"


########
# MAIN
########

for file in os.listdir(source_dir):

    extensions = ['.CR2','.cr2','.jpg','.JPG']

    if file.endswith(tuple(extensions)):

        filename = join(source_dir, file)
        dateinfo = date_taken_info(filename)

        try:
            out_filepath = join(dest_dir, dateinfo[0],dateinfo[1],dateinfo[2])
            out_filename = join(out_filepath, file)

            # Look to see if Folders exists
            if not os.path.exists(out_filepath):
                os.makedirs(out_filepath)
                print "Directories made: {} {} {}".format(dateinfo[0], dateinfo[1],dateinfo[2])

            # If the file exsists in the destination, skip it.
            if not os.path.exists(out_filename):
                print "{} is being moved to {}".format(file, out_filepath)
                shutil.move(filename,out_filename)
            else:
                print "{} was skipped because it already exsists in {}".format(file,out_filepath)

        except:
            pass
