# How the image file is writen to the destination directory
# Construct a folder name from that create date

import datetime
import os

class Writer:
    BASE_DIR_OUT = '/p.out/'

    hashes = {}

    # Get dest directory of file
    # Make sure it exists
    # Move file there, maintaining mod date
    def process(self, image):
        image_date = image.get_create_date()
        image_dir = self.format_date_for_directory_name(image_date)
        image_dir = self.BASE_DIR_OUT + image_dir
        print("Directory {}".format(image_dir))
        rc = self.do_file_hash(image)
        print("hash exists {}".format(rc))
        #self.create_directory(image_dir)
        #self.move(image_dir, self.image.filename)
        print(self.hashes)

    # Given timestamp, determine the directory destination name
    # Folder name format based on date: 2017/01/01
    @staticmethod
    def format_date_for_directory_name(d):
        return d.strftime("%Y/%m/%d")

    # For the given timestamp, make sure the destination directory exists
    def create_directory(self, directory):
        if not os.path.exists(directory):
            print("Create directory ".directory)
            os.makedirs(directory)

    # Given file name, move to the directory destination
    @staticmethod
    def move(directory, filename):
        dest = "{}/{}".format(directory, filename)
        if not os.path.exists(dest):
            print("File destination ".dest)
            os.rename(filename, dest)

    # Does the file hash exist in our list of files?
    def do_file_hash(self, image):
        # look for the hash in our list of hashes
        if image.hash in self.hashes:
            return True
        self.hashes[image.hash] = image.filename
        return False