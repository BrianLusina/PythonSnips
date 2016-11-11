import sys
import re
import os
import shutil
import subprocess


def get_special_paths(directory):
    for file in os.listdir(directory):
        if re.match('\w*(__[a-zA-Z0-9]*__)\.\w*|(__[a-zA-Z0-9]*__)|(__[a-zA-Z0-9]*__)\.\w*', file):
            return os.path.abspath(directory)
    pass


def copy_to(paths, directory):
    for p in paths:
        shutil.copy(p, directory)


def zip_to(paths, zippath):
    pass


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)


if __name__ == "__main__":
    main()
