# How the image file is writen to the destination directory
# Construct a folder name from that create date

import datetime
import os
import shutil
from .image import Image

class Writer:
    BASE_DIR_OUT = '/pics.out/'
    BASE_PROBLEM_DIR = BASE_DIR_OUT+'_problems/'

    recent_date = ''

    def __init__(self, counter):
        self.counter = counter

    # Get dest directory of file
    # Make sure it exists
    # Move file there, maintaining mod date
    def process(self, image):
        #print('.', end='', flush=True)
        self.counter['FILES'] += 1
        image_date = image.get_create_date()
        self.recent_date = image_date
        image_dir = self.format_date_for_directory_name(image_date)
        image_dir = self.BASE_DIR_OUT + image_dir
        self.create_directory(image_dir)
        self.move(image_dir, image)

    # Given timestamp, determine the directory destination name
    # Folder name format based on date: 2017/01/01 year/month/day
    @staticmethod
    def format_date_for_directory_name(d):
        #return d.strftime("%Y/%m/%d")
        return d.strftime("%Y/%m")

    # For the given timestamp, make sure the destination directory exists
    def create_directory(self, directory):
        if not os.path.exists(directory):
            print("Create directory {}".format(directory))
            os.makedirs(directory, exist_ok=True)
            self.counter['DIR_CREATE'] += 1

    # Given file name, move to the directory destination
    def move(self, directory, image):
        dest = "{}/{}".format(directory, os.path.basename(image.filename))
        if not os.path.exists(dest):
            print("File destination {} + {} -> {}".format(directory, image.filename, dest))
            self.create_directory(directory)
            shutil.move(image.filename, dest)
            #shutil.copyfile(image.filename, dest)
            #shutil.copystat(image.filename, dest)
            self.counter['COPY'] += 1
        else:
            dest_image = Image(counter=self.counter, filename=dest)
            if dest_image.get_hash() != image.get_hash():
                # We have a file conflict.  We'll need to kick this file out and try again or rename it
                dest = "{}/{}".format(self.BASE_PROBLEM_DIR, image.filename)
                self.counter['HASH_CONFLICT'] += 1
            else:
                print(f"Same file already exists at {dest_image.filename}. Delete {image.filename}")
                os.remove(image.filename)
