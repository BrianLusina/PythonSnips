"""
a simple demo of Context managers in Python
"""
from array import array
from contextlib import contextmanager
from time import perf_counter


# using context manager decorater, this allows us to create our own context manager
@contextmanager
def timing(label: str):
    """
    times the performance of initializing arrays
    :param label: simple label for logging
    """
    # section before yield is where we write code before the context manager is called
    # in this case we simply record the timestamp before
    t0 = perf_counter()

    # in yield, this is where execution is transferred to the body of your context manager
    # in this case, this is where arrays get created, we can return data as well. In this case we
    # simply return a closure which will calculate the time
    yield lambda: (label, t1 - t0)

    # this is where we write code that will be executed after the context manager finishes
    # in scenerios like file handling, this is where we close files. in this case this is where
    # we get the final time
    t1 = perf_counter()


with timing("Array tests") as total:
    # create the array by passing in a large list
    with timing("Array creation innermul") as inner:
        x = array("d", [0] * 1000000)

    # an alternative array creation strategy, first create the array then increase in size
    # from the output you will realize that creating the array this way is much faster
    with timing("Array creation outermul") as outer:
        y = array("d", [0]) * 1000000

print("Total: [%s]: %.6f s" % total())
print("\t\tTiming: [%s]: %.6f s" % inner())
print("\t\tTiming: [%s]: %.6f s" % outer())
