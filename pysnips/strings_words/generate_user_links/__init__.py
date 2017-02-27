def generate_link(user):
    """
    Generates user links based on the user's name
    appends this to base_url
    :param user: the user name
    :return: a user generated link
    :rtype: str
    """
    base_url = "http://www.codewars.com/users/"
    user = user.replace(" ", "%20")
    return base_url + user
