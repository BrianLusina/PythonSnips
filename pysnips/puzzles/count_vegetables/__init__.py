def count_vegetables(s):
    """
    split string and use Counter object to count each string, convert them to a dictionary
    for each Key value pare in dictionary, add to a list,
    sort the list in descending order by count, then by alphabetical order by using sorted
    return this list
    """
    p = s.split()
    valid = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip",
             "kales", "tomatoes"]
    m = set([(p.count(x), x) for x in p if x in valid])
    return sorted(m, key=lambda tup: (tup[0], tup[1]), reverse=True)
