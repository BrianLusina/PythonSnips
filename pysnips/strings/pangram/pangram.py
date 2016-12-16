import string
def is_pangram(s):
    return not set(string.lowercase) - set(s.lower())