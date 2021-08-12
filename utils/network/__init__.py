from urllib import request
# noinspection PyCompatibility
from urllib.parse import urljoin
# noinspection PyCompatibility
from urllib.request import urlretrieve


class Network(object):
    def __init__(self, url):
        """
        Attributes:
            ufile: file representing the opened url
            text: read file of ufile
            info: display information of the read file
            getType: get the type of the read file from url
            base_url: get the base url as a string
            build_url: builds the url by joining the *base_url* and *url*
        :param url: The url passed in as a string
        """
        self.url = url
        try:
            self.ufile = request.urlopen(self.url)
            self.text = self.ufile.read()
            self.info = self.ufile.info()
            # self.getType = self.info.gettype()
            self.base_url = self.ufile.geturl()
            self.build_url = urljoin(base=self.base_url, url=self.url)
        except IOError:
            print("Problem reading url: %r" % url)

    def download_url(self, filename):
        """
        Downloads the url to the given filename
        :param filename: file name to download data to
        :return: downloaded file object
        """
        return urlretrieve(self.url, filename)

    def __repr__(self):
        return "<NetFile: %r>, Text: %r, Info: %r, Base Url: %r" % (
            self.ufile, self.text, self.info, self.base_url)
