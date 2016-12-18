import re


def word_count(s):
    """
    Create a counter variable to count each word function encounters
    create a regular expression to check for non words and words hated
     "a", "the", "on", "at", "of", "upon", "in" "as",
    """

    counter = 0
    words = r"\W+|^(a)$|^(as)$|^(at)$|^(of)$|^(in)$|^(on)$|^(the)$|^(upon)$"
    count = len(re.findall(words, s))
    for x in s.split():
        print(x, re.findall(pattern=r"[a-zA-Z]", string=x))
        if not re.match(words, x):
            counter += 1
    return counter
