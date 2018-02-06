# Given image file name
# Get the exif meta data create date
# Get md5 hash of file contents
# Use file writer class to write the file to destination based on date

import PIL.Image
from PIL.ExifTags import TAGS
from pprint import pprint
import datetime
import hashlib

class Image:
    BLOCKSIZE = 65536

    hash = ''


    def __init__(self, filename):
        self.filename = filename

    def get_create_date(self):
        exif = self.get_exif(self.filename)
        return self.get_origin_date(exif)

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

    def get_hash(self):
        if self.hash:
            return self.hash
        hasher = hashlib.md5()
        with open(self.filename, 'rb') as afile:
            buf = afile.read(self.BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(self.BLOCKSIZE)
        self.hash = hasher.hexdigest()
        return self.hash
