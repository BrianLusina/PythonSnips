from PythonUtilities.Network import Network
from pprint import pprint

url = input("Enter a url: ")

net = Network(str(url))

# downloads the url to current directory
net.download_url("download.html")

pprint(net)
