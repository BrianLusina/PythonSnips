import re


def email_parser(email):
    r2 = re.match(pattern=r'(\w+|\d+|[a-zA-Z0-9]+)@((\w+\.)+(com))', string=email)
    return "<Username: %r>, <Domain: %r>" % (r2.group(1), r2.group(2))
