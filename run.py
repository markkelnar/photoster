#!/usr/bin/env python3

# input
# dir
# file

# if image
# get image meta data

from pathlib import Path

p = Path('.')
[x for x in p.iterdir() if x.is_dir()]
