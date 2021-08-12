from pprint import pprint

from PythonUtilities.Network import Network

url = input("Enter a url: ")

net = Network(str(url))

# downloads the url to current directory
net.download_url("download.html")

pprint(net)
