import re


def hey(what):
    what = what.strip()
    # silence
    if len(what) == 0:
        return "Fine. Be that way!"
    que = r'(\w|\W)+\?$'
    # shouting
    if what.isupper() and not what.islower():
        return 'Whoa, chill out!'
    # question
    if re.match(que, what):
        return 'Sure.'
    # everything else
    else:
        return 'Whatever.'
