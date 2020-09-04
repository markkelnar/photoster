#!/usr/bin/env python3

# input file

# if image
# get image meta data

import os
import re
from collections import Counter
import sys

from library.image import Image
from library.writer import Writer

print("Process images")

counter = Counter()
writer = Writer(counter=counter)

# If ends in trash, skip it
def if_skip(name):
    if re.search('\$folder\$$', name):
        return True
    return False

name=sys.argv[1]
print("FILE -> ", name)
if if_skip(name):
    print("SKIP NAME ", name)
    counter['SKIPPED'] += 1
print(name)
img = Image(filename=name, counter=counter)
writer.process(img)

print("\n-----")
for i,v in counter.items():
    print(i, v)
