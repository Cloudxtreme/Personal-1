"""
This is the basis of a script for pulling EXIF data from images
https://pypi.python.org/pypi/ExifRead
"""

import exifread

f = open("/Users/aschoonover/Downloads/_MG_9862.CR2", "rb")
tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print "Key: %s, value %s" % (tag, tags[tag])
