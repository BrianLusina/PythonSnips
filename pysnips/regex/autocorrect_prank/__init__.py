import re


def auto_correct(input_):
    res = []
    for word in input_.split(" "):
        res.append(re.sub('^(u|U)$|(^((Y|y)(o|O)(u)*)$)',
                          repl="your sister",
                          string=word,
                          count=1))
    return " ".join(res)


print(auto_correct("I miss you!"))


