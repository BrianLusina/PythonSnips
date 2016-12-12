import os


class FileMatcher(object):
    """
    File matcher class that copies files to their respective directories, creates directories if none exist
    """

    def __init__(self, dir):
        """
        Creates a new FileMatcher object
        """
        self.dir = dir

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

    