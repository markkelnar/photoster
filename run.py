#!/usr/bin/env python3

# input
# dir
# file

# if image
# get image meta data

import os
import re
from image import Image
from writer import Writer
from collections import Counter

print("Process images")

counting = ['FILES', 
    'COPY', 
    'HASH', 
    'DIR_CREATE', 
    'IMAGE', 
    'NOT_IMAGE', 
    'NO_IMAGE_INFO', 
    'TIME_FROM_PATH', 
    'TIME_FROM_MOD',
    'HASH_CONFLICT',
    'SKIPPED'
    ]
print("TRACE")
counter = Counter()
writer = Writer(counter=counter)

# If ends in trash, skip it
def if_skip(name):
    if re.search('\$folder\$$', name):
        return True
    return False

for (dirpath, dirnames, filenames) in os.walk('/pics.in/',followlinks=True):
    print(dirpath, dirnames, filenames)
    for name in filenames:
        print(name)
        full_filename = os.path.join(dirpath, name)
        #print("FILE -> ", full_filename)
        if if_skip(name):
            print("SKIP NAME ", name)
            counter['SKIPPED'] += 1
            continue
        #print(full_filename)
        print('.', end='', flush=True)
        img = Image(filename=full_filename, counter=counter)
        writer.process(img)

print("\n-----")
for i,v in counter.items():
    print(i, v)
