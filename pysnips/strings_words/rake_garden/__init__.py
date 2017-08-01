import re


def rake_garden(garden):
    garden_list = garden.split(" ")
    raked = []
    for item in garden_list:
        if not re.match("gravel|rock", item):
            item = "gravel"
            raked.append(item)
        else:
            raked.append(item)
    return " ".join(raked)


VALID = {'gravel', 'rock'}


def rake_garden_2(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())
