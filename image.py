#!/usr/bin/env python3

import PIL.Image
from PIL.ExifTags import TAGS
from pprint import pprint
import datetime

class Image:
    def __init__(self, filename):
        print(filename)
        self.filename = filename

    def process(self):
        exif = self.get_exif(self.filename)
        datetime = self.get_origin_date(exif)
        folder_name = self.get_folder_from_date(datetime)

    @staticmethod
    def get_exif(fn):
        ret = {}
        img = PIL.Image.open(fn)
        info = img._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if 'MakerNote' == decoded:
                continue
            ret[decoded] = value
        return ret

    # 'DateTimeOriginal': '2016:09:03 17:47:51'
    @staticmethod
    def get_origin_date(info):
        t = info['DateTimeOriginal']
        return datetime.datetime.strptime(t, "%Y:%m:%d %H:%M:%S")

    # Folder name format based on date: 2017_01_01
    @staticmethod
    def get_folder_from_date(d):
        return d.strftime("%Y_%m_%d")
