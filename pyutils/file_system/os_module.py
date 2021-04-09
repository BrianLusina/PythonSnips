from pprint import pprint

from PyUtilities.FileSystem import MyFileSystem

# fetch the file names in current directory
# 1 (.) dot refers to the current directory, 2 dots (..) takes it a directory higher

current_dir = MyFileSystem(".")
upper_level_dir = MyFileSystem('..')

# current directory
pprint(upper_level_dir.read_current_dir())
pprint(current_dir.read_current_dir())

# make the paths
pprint(current_dir.make_path())
pprint(upper_level_dir.make_path())

# make absolute paths
pprint(current_dir.make_absolute_path())
pprint(upper_level_dir.make_absolute_path())

# get directory names and base names
pprint(upper_level_dir.obtain_dir_basenames())
pprint(current_dir.obtain_dir_basenames())
