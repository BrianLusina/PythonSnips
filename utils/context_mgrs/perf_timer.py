from contextlib import contextmanager
from time import perf_counter


# using context manager decorator, this allows us to create our own context manager
@contextmanager
def timing(label: str):
    """
    times the performance of running a function
    :param label: simple label for logging
    """
    # section before yield is where we write code before the context manager is called
    # in this case we simply record the timestamp before
    t0 = perf_counter()

    # in yield, this is where execution is transferred to the body of your context manager
    # for example, where arrays get created or where we can return data. In this case we
    # simply return a closure which will calculate the time
    yield lambda: (label, t1 - t0)

    # this is where we write code that will be executed after the context manager finishes
    # in scenarios like file handling, this is where we close files. in this case this is where
    # we get the final time
    t1 = perf_counter()
