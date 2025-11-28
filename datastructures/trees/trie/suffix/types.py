from typing import Tuple
import sys


# Type alias for the best word info: (length, original_index)
WordInfo = Tuple[int, int]
# Initialize with a very large length to ensure the first word always wins
INF_WORD_INFO: WordInfo = (sys.maxsize, sys.maxsize)
