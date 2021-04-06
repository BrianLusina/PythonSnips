import os
import shutil


class MyFileSystem(object):
    """
    Simple filesystem to read files from directories it receives
    """

    def __init__(self, directory):
        self.directory = directory

    def read_current_dir(self):
        """
        Builds a list of files from the given directory
        If path is non existent, return the current directory
        :return: A list of all files in the given directory
        """
        return os.listdir(self.directory) if self.is_path_valid() else "."

    def make_path(self):
        """
        Makes an absolute path from the given directory
        :return:
        """
        if self.read_current_dir():
            return [os.path.join(self.directory, files) for files in self.read_current_dir()]
        return False

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

    def is_path_valid(self, path=None):
        """
        Checks if the given path is valid
        :return: True/False value:rtype bool
        """
        return os.path.exists(self.directory)

    @staticmethod
    def make_dir(dir_name):
        """
        :param dir_name: Name of directory to be made
        :return: return the currently created directory name
        """
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            # noinspection PyCompatibility
            raise FileExistsError("File already exists")

    def make_copy(self, from_path, to_path):
        """
        Copies a file to the destination path
        :param to_path: Path to copy the file to
        :param from_path The path to copy from
        :return:
        """
        # check if destination path exists
        if self.is_path_valid(path=to_path):
            shutil.copy(from_path, to_path)
        else:
            print("Destination path does not exist")
