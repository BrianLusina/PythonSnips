import os


class RemovalService(object):
    """Service for removing objects from the file system"""

    @staticmethod
    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):
    """Upload service that depends on Removal Service"""

    def __init__(self, removal_service):
        """
        Creates an Upload Service object
        """
        self.removal_service = removal_service

    def upload_complete(self, filename):
        """
        method to remove a file
        """
        self.removal_service.rm(filename)
