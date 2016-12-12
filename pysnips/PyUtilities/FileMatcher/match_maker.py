from pysnips.PyUtilities.FileMatcher import FileMatcher
from pprint import pprint

file_matcher = FileMatcher("..", "..")

pprint(file_matcher.get_dirs_in_destination())
pprint(file_matcher.list_files_in_dir())
