import re

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


def acronym_buster(message):
    """
    Find the first group of words that is in all caps
    check if it is in the ACRONYMS dict
    if it is, return the first occurrence of the acronym
    else return [acronym] is an acronym. I do not like acronyms. Please remove them from your email.
    :param message: The message to check
    :return:
    """
    words = message.split()
    result, res, forbiden = [], [], []
    for word in words:
        if re.match("[A-Z]{3,}", word) and word in ACRONYMS.keys():
            word_new = re.sub("([A-Z]{3,})", ACRONYMS[word], word)
            res.append(word_new)
            result.append(word_new)
        elif re.match("[A-Z]{3,}", word) and word not in ACRONYMS.keys():
            return word + " is an acronym. I do not like acronyms. Please remove them from your email."
        else:
            res.append(word)
    return " ".join(res).capitalize()

# acronym_buster("I am IAM so will be OOO until EOD")
# "SMB is an acronym. I do not like acronyms. Please remove them from your email.
print(acronym_buster("We're looking at SMB on SM DMs today"))
print(acronym_buster("WAH"), "Work at home")
