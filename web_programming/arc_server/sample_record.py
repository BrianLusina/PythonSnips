"""
Sample client for uinames.com that fetches a fake user and parses the data.
the data is fetched using requests module
"""
import requests


def sample_record():
    r = requests.get("http://uinames.com/api/?ext&region=kenya", timeout=2.0)
    name = r.json()["name"]
    surname = r.json()["surname"]
    pin = r.json()["credit_card"]["pin"]

    return "My name is {} {} and the PIN on my card is {}".format(name, surname, pin)


print(sample_record())
