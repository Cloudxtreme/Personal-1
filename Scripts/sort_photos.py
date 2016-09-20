#!/usr/bin/env python
import exifread
from exifread import process_file, __version__
import datetime
import hashlib
import os
import shutil
import subprocess

# source_dir = raw_input("Source Directory: ").rstrip('/')
source_dir = "/Users/aschoonover/Downloads"
# dest_dir = raw_input("Destination Directory: ").rstrip('/')
dest_dir = source_dir + os.sep + "Test"

def date_taken_info(filename):

        open_file = open(filename, 'rb')
        tags = exifread.process_file(open_file, stop_tag='Image DateTime', details=False)

        datetaken_string = tags['Image DateTime']
        datetaken_object = datetime.datetime.strptime(datetaken_string.values, '%Y:%m:%d %H:%M:%S')

        #creates a dict
        day = str(datetaken_object.day).zfill(2)
        month = str(datetaken_object.month).zfill(2)
        year = str(datetaken_object.year)

        output = [year, month, day]
        return output


for file in os.listdir(source_dir):
    if file.endswith('.CR2'):

        filename = source_dir + os.sep + file
        dateinfo = date_taken_info(filename)

        try:
            out_filepath = dest_dir + os.sep + dateinfo[0] + dateinfo[1] + dateinfo[2]
            out_filename = out_filepath + file

            if not os.path.exists(out_filepath):
                os.makedirs(out_filepath)

            shutil.copy2(filename,out_filename)

        except:
            None
