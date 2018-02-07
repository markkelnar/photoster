# How the image file is writen to the destination directory
# Construct a folder name from that create date

import datetime
import os
import shutil
from image import Image

class Writer:
    BASE_DIR_OUT = '/p.out/'
    BASE_PROBLEM_DIR = BASE_DIR_OUT+'_problems/'

    hashes = {}

    def __init__(self, counter):
        self.counter = counter

    # Get dest directory of file
    # Make sure it exists
    # Move file there, maintaining mod date
    def process(self, image):
        self.counter['FILES'] += 1
        image_date = image.get_create_date()
        image_dir = self.format_date_for_directory_name(image_date)
        image_dir = self.BASE_DIR_OUT + image_dir
        #print("Directory {}".format(image_dir))
        rc = self.do_file_hash(image)
        self.create_directory(image_dir)
        self.move(image_dir, image)
        self.counter['HASH'] += 1

    # Given timestamp, determine the directory destination name
    # Folder name format based on date: 2017/01/01
    @staticmethod
    def format_date_for_directory_name(d):
        return d.strftime("%Y/%m/%d")

    # For the given timestamp, make sure the destination directory exists
    def create_directory(self, directory):
        if not os.path.exists(directory):
            print("Create directory {}".format(directory))
            os.makedirs(directory)
            self.counter['DIR_CREATE'] += 1

    # Given file name, move to the directory destination
    def move(self, directory, image):
        dest = "{}/{}".format(directory, os.path.basename(image.filename))
        # If dest exists, does hash match this file?
        if os.path.exists(dest):
            dest_image = Image(counter=self.counter, filename=dest)
            if dest_image.get_hash() != image.get_hash():
                # We have a file conflict.  We'll need to kick this file out and try again or rename it
                dest = "{}/{}".format(self.BASE_PROBLEM_DIR, image.filename)
        if not os.path.exists(dest):
            print("File destination {} + {} -> {}".format(directory, image.filename, dest))
            #os.rename(filename, dest)
            shutil.copyfile(image.filename, dest)
            shutil.copystat(image.filename, dest)
            self.counter['COPY'] += 1

    # Does the file hash exist in our list of files?
    def do_file_hash(self, image):
        # look for the hash in our list of hashes
        h = image.get_hash()
        if h in self.hashes:
            return True
        self.hashes[h] = image.filename
        return False