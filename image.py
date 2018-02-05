#!/usr/bin/env python3

import PIL.Image
from PIL.ExifTags import TAGS
from pprint import pprint

def get_exif(image):
    ret = {}
    info = image._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if 'MakerNote' == decoded:
            continue
        ret[decoded] = value
    return ret


img = PIL.Image.open('IMG_8622.JPG')
exif_data = get_exif(img)
pprint(exif_data)

