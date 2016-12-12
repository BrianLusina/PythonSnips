import os
import shutil


class FileMatcher(object):
    """
    File matcher class that copies files to their respective directories, creates directories if none exist
    """

    def __init__(self, dir, destination):
        """
        Creates a new FileMatcher object
        :param dir, the current directory with the files
        :param destination, the destination directory where the files are to be copied to
        """
        self.dir = dir
        self.destination = destination

    def list_files_in_dir(self):
        """
        Lists all file names in the current directory,
        Loops through the file name list, saving only file names that are not directories saving them in a
        list.
        :return: List of files in directory
        """
        # lists all file names including directories and files
        filenames = os.listdir(self.dir)
        return [file for file in filenames if not os.path.isdir(file)]

    def get_dirs_in_destination(self):
        """
        Gets the directories in the destination directory and saves their absolute paths in a dictionary
        They key will be the name of the dir, the value will be the absolute path
        :return: dictionary of the directories in the destination directories
        """
        # list all the files in the destination directory
        dirnames = os.listdir(self.destination)
        directories = {}
        for dir in dirnames:
            if os.path.isdir(dir) and dir not in directories:
                directories[dir] = os.path.abspath(dir)

        return directories
