# Given image file name
# Get the exif meta data create date
# Get md5 hash of file contents
# Use file writer class to write the file to destination based on date

import datetime
import hashlib
import re
import os

from exiftool import ExifToolHelper

class Image:
    BLOCKSIZE = 65536
    DEFAULT_DATE_UNKNOWN = '1950:01:01 01:01:01'
    DEFAULT_DATE_IMAGE = '1951:01:01 02:02:02'

    hash = ''

    exif = None

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
        with ExifToolHelper() as et:
            # for d in et.get_metadata(fn):
            #     for k, v in d.items():
            #         print(f"Dict: {k} = {v}")
            for d in et.get_tags(fn, tags=["EXIF:DateTimeOriginal", "QuickTime:CreationDate", "File:FileType", "File:FileTypeExtension"]):
                self.exif = d
        # print(self.exif)
        self.counter['FILE_TYPE_' + self.exif["File:FileType"]] += 1
        # 'EXIF:DateTimeOriginal': '2016:09:06 19:34:07'
        # 'QuickTime:CreationDate': '2016:09:05 13:11:08'
        if 'EXIF:DateTimeOriginal' in self.exif:
            return d['EXIF:DateTimeOriginal']
        if 'QuickTime:CreationDate' in self.exif:
            return d['QuickTime:CreationDate']

    # @param time '2016:09:03 17:47:51-05:00'
    @staticmethod
    def format_create_date(time):
        dt = None
        try:
            dt = datetime.datetime.strptime(time, "%Y:%m:%d %H:%M:%S")
        except ValueError as e:
            dt = datetime.datetime.strptime(time, "%Y:%m:%d %H:%M:%S%z")
        return dt

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
        match = re.search('\/(\d\d\d\d)\/(\d\d)\/(\d\d)', filename)
        if match:
            time = "{}:{}:{} 03:03:03".format(match.group(1), match.group(2), match.group(3))
            return time
        match = re.search('\/(\d\d\d\d)\/(\d\d)', filename)
        if match:
            time = "{}:{}:01 03:03:03".format(match.group(1), match.group(2))
            return time
        raise Exception('No time from path')

    @staticmethod
    def get_time_from_mod_time(filename):
        time = os.path.getmtime(filename)
        return datetime.datetime.utcfromtimestamp(time).strftime('%Y:%m:%d %H:%M:%S')

    def get_file_extension(self, filename):
        return self.exif["File:FileType"].lower()
