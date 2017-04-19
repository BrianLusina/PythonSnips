import re


def xoxo(stringer):
    """
    check whether the string x or the string o is present, if so, check the count
    else, return false
    """
    stringer = stringer.lower()
    if stringer.find("x") != -1 and stringer.find("o") != -1:
        return stringer.count("x") == stringer.count("o")
    return False


def xoxo_reg(stringer):
    X = re.findall(r'(o)(x)(o)|\s+(X|x)\s+', stringer, re.IGNORECASE)
    O = re.findall(r"(x)(o|O)(x)|\s+(O|o)\s+", stringer, re.IGNORECASE)
    return len(X) == len(O)
