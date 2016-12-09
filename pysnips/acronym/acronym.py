import re


def abbreviate(phrase):
    return ''.join(word[0].upper() for word in re.findall(pattern="[A-Z]+[a-z]*|[a-z]+", string=phrase))
