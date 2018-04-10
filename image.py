# Given image file name
# Get the exif meta data create date
# Get md5 hash of file contents
# Use file writer class to write the file to destination based on date

import datetime
import hashlib
import re
import os

import pyexifinfo


class Image:
    BLOCKSIZE = 65536
    DEFAULT_DATE_UNKNOWN = '1950:01:01 01:01:01'
    DEFAULT_DATE_IMAGE = '1951:01:01 02:02:02'

    hash = ''

    def __init__(self, counter, filename):
        self.counter = counter
        self.filename = filename

    def get_create_date(self):
        time = None
        try:
            time = self.get_date_from_exif(self.filename)
            self.counter['TIME_FROM_EXIF'] += 1
        except OSError as e:
            # Not an image
            self.counter['NOT_IMAGE'] += 1
        except Exception as e:
            self.counter['NO_IMAGE_INFO'] += 1            

        try:
            if not time:
                time = self.get_time_from_path(self.filename)
                self.counter['TIME_FROM_PATH'] += 1
        except Exception as e:
            time = self.get_time_from_mod_time(self.filename)
            self.counter['TIME_FROM_MOD'] += 1
        return self.format_create_date(time=time)

    def get_date_from_exif(self, fn):
        self.counter['FILE_TYPE_'+pyexifinfo.fileType(fn)] += 1
        d = pyexifinfo.get_json(fn)[0]
        # 'EXIF:DateTimeOriginal': '2016:09:06 19:34:07'
        # 'QuickTime:CreateDate': '2016:09:05 13:11:08'
        if 'EXIF:DateTimeOriginal' in d:
            return d['EXIF:DateTimeOriginal']
        if 'QuickTime:CreateDate' in d:
            return d['QuickTime:CreateDate']

    # @param time '2016:09:03 17:47:51'
    @staticmethod
    def format_create_date(time):
        return datetime.datetime.strptime(time, "%Y:%m:%d %H:%M:%S")

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

    # If can't get image file info, because it doesn't have it or it's a video file,
    # See if the file name has a date in the path, like DDDD/DD/DD or YYYY/MM/DD
    def get_time_from_path(self, filename):
        match = re.search('(\d\d\d\d)\/(\d\d)\/(\d\d)', filename)
        if match:
            time = "{}:{}:{} 03:03:03".format(match.group(1), match.group(2), match.group(3))
            return time
        match = re.search('(\d\d\d\d)\/(\d\d)', filename)
        if match:
            time = "{}:{}:01 03:03:03".format(match.group(1), match.group(2))
            return time
        raise Exception('No time from path')

    @staticmethod
    def get_time_from_mod_time(filename):
        time = os.path.getmtime(filename)
        return datetime.datetime.utcfromtimestamp(time).strftime('%Y:%m:%d %H:%M:%S')
