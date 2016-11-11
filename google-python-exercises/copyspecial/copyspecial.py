import sys
import re
import os
import shutil
# Python 2.x/Python 3.x
try:
    import commands
except ImportError:
    import subprocess


def get_special_paths(directory):
    """
    Given a dirname, returns a list of all its special files.
    """
    files = os.listdir(directory)
    return [os.path.abspath(os.path.join(directory, file))
            for file in files if re.match(r'__(\w+)__', file)]


def copy_to(paths, to_dir):
    """
    :param paths: List of paths to copy from
    :param directory: paths to copy to
    :return:
    """
    # if path does not exist, make the dir
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for p in paths:
        # get the base file name from the path
        file_name = os.path.basename(paths)
        # copy each file to the new destination
        shutil.copy(p, os.path.join(p, file_name))


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
