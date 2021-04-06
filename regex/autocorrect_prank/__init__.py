import re


def auto_correct(input_):
    res = []
    for word in input_.split(" "):
        res.append(re.sub('^(u|U)$|(^((Y|y)(o|O)(u)*)$|(you))',
                          repl="your sister",
                          string=word,
                          count=1))
    return " ".join(res)
