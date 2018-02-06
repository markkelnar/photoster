#!/usr/bin/env python3

# input
# dir
# file

# if image
# get image meta data

import os
from image import Image
from writer import Writer
from collections import Counter

print("Process images")

counting = ['FILES', 'COPY', 'HASH', 'DIR_CREATE', 'IMAGE', 'NOT_IMAGE', 'NO_IMAGE_INFO']
counter = Counter()
writer = Writer(counter=counter)

for (dirpath, dirnames, filenames) in os.walk('/p.in/',followlinks=True):
    for name in filenames:
        full_filename = os.path.join(dirpath, name)
        #print("FILE -> ", full_filename)
        img = Image(filename=full_filename, counter=counter)
        writer.process(img)

for c in counting:
    print(c, counter[c])
