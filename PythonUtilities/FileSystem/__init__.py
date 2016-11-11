import os


class MyFileSystem(object):
    """
    Simple filesystem to read files from directories it receives
    """

    def __init__(self, directory):
        self.directory = directory

    def read_current_dir(self):
        """
        Builds a list of files from the given directory
        :return: A list of all files in the given directory
        """
        return os.listdir(self.directory)

    def make_path(self):
        """
        Makes an absolute path from the given directory
        :return:
        """
        return [os.path.join(self.directory, files) for files in self.read_current_dir()]

    def make_absolute_path(self):
        """
        :return: An absolute path for the given directory
        """
        return os.path.abspath(self.directory)

    def obtain_dir_basenames(self):
        """
        Fetches the directory and base names of files in current directory
        :return: dict with the key as the directory name and value as the base name
        """
        return {
            "Dir: " + os.path.dirname(self.make_absolute_path()): "Base" + os.path.basename(self.make_absolute_path())
            }
