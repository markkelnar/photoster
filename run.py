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

print("Image date {}".format(img.get_create_date()))
print("Image hash {}".format(img.get_hash()))

print("Image hash {}".format(img.get_hash()))

writer = Writer()
writer.process(img)
writer.process(img)
