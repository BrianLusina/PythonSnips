"""
Using functools.wraps to avoid losing decorated functions metadata, __doc__, __name__ (or __qualname__)
"""
from functools import wraps


def uppercase(func):
    @wraps(func)
    def wrapper():
        return func().upper()

    return wrapper


@uppercase
def greet():
    """Return a friendly greeting"""
    return "hello"


if __name__ == "__main__":
    greet()
