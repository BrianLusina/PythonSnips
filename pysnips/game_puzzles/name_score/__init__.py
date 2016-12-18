alpha = {'ABCDE': 1, 'FGHIJ': 2, 'KLMNO': 3, 'PQRST': 4, 'UVWXY': 5}


def name_score(name):
    sc = 0
    for x in alpha.keys():
        for y in name:
            if y.upper() in x:
                sc += alpha.get(x)
    return {name: sc}
