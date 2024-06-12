from typing import Callable
import time


def func_timer(func: Callable) -> Callable:
    """
    Decorator function that times the execution of a function
    Args:
        func: Callable function to time
    Returns:
        Callable: function that wraps around the function to time
    """

    def timer(*args, **kwargs):
        """
        Times a given function and passes in the arguments called on the function
        @param args:
        @param kwargs:
        @return:
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution."
        print(msg.format(func=func.__name__, time=runtime))
        return value

    return timer
