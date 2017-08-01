import re
from functools import reduce

ACRONYMS = {
    'KPI': "key performance indicators",
    'EOD': "the end of the day",
    'TBD': "to be decided",
    'WAH': "work at home",
    'IAM': "in a meeting",
    'OOO': "out of office",
    'NRN': "no reply necessary",
    'CTA': "call to action",
    'SWOT': "strengths, weaknesses, opportunities and threats",
}

ACRONYM_PATTERN = re.compile(r"\b[A-Z]{3,}\b")
CAPITAL_PATTERN = re.compile(r"(?:\. |^)([a-z])")
CAPITAL_FIX = lambda match: "{}".format(match.group(0).upper())


def acronym_buster(message):
    """
    Find the first group of words that is in all caps
    check if it is in the ACRONYMS dict
    if it is, return the first occurrence of the acronym
    else return [acronym] is an acronym. I do not like acronyms. Please remove them from your email.
    :param message: The message to check
    :return: new string with the acronyms replaced with full words
    :rtype:str
    """
    message = reduce(lambda msg, item: msg.replace(*item), ACRONYMS.items(), message)

    try:
        # find all matching groups with .finditer using next and get the first acronym that is not allows
        acronym = next(ACRONYM_PATTERN.finditer(message)).group(0)
        return "{} is an acronym. I do not like acronyms. Please remove them from your email.".format(acronym)
    except StopIteration:
        return CAPITAL_PATTERN.sub(CAPITAL_FIX, message)
