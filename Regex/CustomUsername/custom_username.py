import re

emailAddress = input("Please enter your email address: ")


def email_parser(email):
    r2 = re.match(pattern=r'(\w+)@((\w+\.)+(com))', string=email)
    return "<Username: %r>, <Domain: %r>" % (r2.group(1),  r2.group(2))

print(email_parser(email=emailAddress))



