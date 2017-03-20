import os


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
