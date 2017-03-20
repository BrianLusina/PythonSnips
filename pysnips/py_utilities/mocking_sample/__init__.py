import os


class RemovalService(object):
    """Service for removing objects from the file system"""

    @staticmethod
    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)
