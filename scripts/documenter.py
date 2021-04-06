def document_me(function):
    """
    Returns the documentation for a given function
    :param function: takes in a function
    :return: the documentation of the function
    """
    return function.__doc__


# demo
print(document_me(abs))
print(document_me(int))
