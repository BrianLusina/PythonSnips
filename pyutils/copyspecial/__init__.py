import os
import re
import shutil
import sys

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
    :param to_dir:
    :param paths: List of paths to copy from
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
    cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
    print("Command I'm going to do:" + cmd)
    try:
        (status, output) = subprocess.getstatusoutput(cmd)
    except NameError:
        (status, output) = commands.getstatusoutput(cmd)
    # If command had a problem (status is non-zero),
    # print( its output to stderr and exit.
    if status:
        sys.stderr.write(output)
        sys.exit(1)


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

    # +++your code here+++
    # Call your functions
    # LAB(begin solution)

    # Gather all the special files
    paths = []
    for dirname in args:
        paths.extend(get_special_paths(dirname))

    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print('\n'.join(paths))
        # LAB(end solution)


if __name__ == "__main__":
    main()
