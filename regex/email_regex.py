import re


def is_email_valid(email):
    """
    Checks if a certain email address follows the given conventional pattern of
     username@domain.extension
    :param email: given email address
    :return: True if the given email address is valid, False otherwise
    :rtype: bool
    """
    return True if re.fullmatch(r'^[a-zA-Z0-9][\w\-._]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}|\.[a-zA-Z]{1,3}\.[a-zA-Z]{1,3}$',
                                email) else False
