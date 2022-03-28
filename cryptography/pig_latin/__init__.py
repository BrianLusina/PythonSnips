import re

cons = re.compile('^([^aeiou]?qu|[^aeiou]+)([a-z]*)')
cons_with_y = re.compile('^([^aeiou]+)y([a-z]*)')
vowel = re.compile('^([aeiou]|y[^aeiou]|xr)[a-z]*')


def split_initial_consonant_sound(word):
    match_with_y = cons_with_y.match(word)
    match = cons.match(word)
    if match_with_y:
        return match_with_y.group(1), f"y{match_with_y.group(2)}"
    if match:
        return match.groups()


def starts_with_vowel_sound(word):
    return vowel.match(word) is not None


def translate(words):
    res = []
    for w in words.split():
        if starts_with_vowel_sound(w):
            res.append(w + "ay")
        else:
            head, tail = split_initial_consonant_sound(w)
            res.append(tail + head + "ay")
    return " ".join(res)


def pig_it(text):
    return " ".join(x.replace(x[0], "") + x[0] + "ay" for x in text.split(" ") if re.match('\w+', x))
