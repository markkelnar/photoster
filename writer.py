import datetime
import os

class Writer:
    BASE_DIR_OUT = '/p.out/'

    def __init__(self, filename, date):
        self.filename = filename
        self.date = date

    # get dest directory of file
    # make sure it exists
    # move file there, maintaining mod date
    def process(self):
        directory = self.format_date_for_directory_name(self.date)
        directory = self.BASE_DIR_OUT + directory
        print("Directory {}".format(directory))
        #self.create_directory(directory)
        #self.move(directory, self.filename)

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
