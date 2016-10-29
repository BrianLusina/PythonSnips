import re


def autocorrect(input_):
    return re.sub(
        '^(u|U)$|^(U|u)\s+([a-zA-Z0-9])+$|^[a-zA-Z]+\s+(u|U)$|^((Y|y)(o|O)(u))$|^((Y|y)(o|O)(u)*)\s+[a-zA-Z0-9]*$|^[a-zA-Z0-9]*((Y|y)(o|O)(u)*)$',
        repl="your sister",
        string=input_,
        count=1)
