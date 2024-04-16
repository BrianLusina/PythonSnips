"""
a simple demo of Context managers in Python
"""

from array import array
from perf_timer import timing

with timing("Array tests") as total:
    # create the array by passing in a large list
    with timing("Array creation innermul") as inner:
        x = array("d", [0] * 1000000)

    # an alternative array creation strategy, first create the array then increase in size
    # from the output you will realize that creating the array this way is much faster
    with timing("Array creation outermul") as outer:
        y = array("d", [0]) * 1000000

if __name__ == "__main__":
    print("Total: [%s]: %.6f s" % total())
    print("\t\tTiming: [%s]: %.6f s" % inner())
    print("\t\tTiming: [%s]: %.6f s" % outer())
