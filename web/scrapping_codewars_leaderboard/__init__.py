# noinspection PyCompatibility
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = 'https://www.codewars.com/users/leaderboard'


# todo: find the solution!
def solution():
    # list to store the leaders
    position = []

    # retrieve the file and save it as html
    urlretrieve(url, "leaderboard.html")

    # open the file in a context and store it's contents
    with open("leaderboard.html") as html:
        file = html.read()

    # read and parse the file with Beautiful soup
    soup = BeautifulSoup(file, "html.parser")

    # extract all data from table containing the leaderboard
    rank = 1
    for link in soup.find_all("tr"):
        leader = {}
        try:
            leader["name"] = link["data-username"]
            leader["rank"] = rank
            # get the clan
            for td in link.find_all("td"):
                leader["clan"] = td.string
                leader["honor"] = td.string
            rank += 1
        except KeyError as ke:
            print(ke)
        position.append(leader)
    return position


print(solution())
