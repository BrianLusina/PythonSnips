try:
    # noinspection PyCompatibility
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


class DataDownload(object):
    """
    Downloads data from the web and stores them in a file
    """

    def __init__(self, url, file_name):
        """
        Creates a new DataDownload object
        :param url: url to download the data from
        :param file_name: file name where to store the data
        """
        self.url = url
        self.file_name = file_name

    def download(self):
        """
        Performs actual file download.
        Retrieves the url and stores the data in file
        :return a tuple object with the file name and the http object
        :rtype: tuple
        """
        return urlretrieve(self.url, self.file_name)
