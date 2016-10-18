#!/usr/bin/env python
import exifread
import datetime
import os
import shutil
import calendar
import filecmp

"""
v1. A Script to take all CR2 files off the camera card
    and move them to a folder in the Photos folder.
    Format for destination is [year]/[num_month - name_month]/[date]
"""

# source_dir = raw_input("Source Directory: ").rstrip('/')
# dest_dir = raw_input("Destination Directory: ").rstrip('/')
source_dir = "/Users/aschoonover/Downloads/photo-move-test"
dest_dir = source_dir + os.sep + "post_move"

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


for file in os.listdir(source_dir):
    if file.endswith('.CR2'):

        filename = source_dir + os.sep + file
        dateinfo = date_taken_info(filename)

        try:
            out_filepath = dest_dir + os.sep + dateinfo[0] + os.sep + dateinfo[1] + os.sep + dateinfo[2]
            out_filename = out_filepath + os.sep + file

            # Look to see if Folders exists
            if not os.path.exists(out_filepath):
                os.makedirs(out_filepath)
            else:
                continue

            if not os.path.exists(out_filename):
                print "{} has been moved to {}".format(out_filename,out_filepath)
                shutil.copy2(filename,out_filename)
            else:
                continue

        except:
            print "There was an error"
