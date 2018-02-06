#!/usr/bin/env python3

# input
# dir
# file

# if image
# get image meta data

from image import Image
from writer import Writer

print("Hello you")

file = '/p.in/IMG_8622.JPG'
img = Image(file)
d = img.get_create_date()
print("Image date {}".format(d))

writer = Writer(file, d)
writer.process()
