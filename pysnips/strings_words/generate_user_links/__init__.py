try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


def generate_link(user):
    """
    Generates user links based on the user's name
    appends this to base_url
    :param user: the user name
    :return: a user generated link
    :rtype: str
    """
    return "http://www.codewars.com/users/" + quote(user)
