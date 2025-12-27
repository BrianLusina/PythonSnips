from copy import copy
from typing import List, Set, Tuple
from algorithms.backtracking.word_search.point import Point
from algorithms.backtracking.word_search.constants import PLANE_LIMITS
from datastructures.trees.trie import Trie, TrieNode


class WordSearch:
    def __init__(self, puzzle):
        """
        Creates a new word search object
        :ivar self.width will be the length of the width for this word-search object, which is the length of the
        first item in the list.
        It is assumed that all items will have same length
        :ivar self.height will be the height of thw object, in this case, just the length of the list
        :param puzzle: the puzzle which will be a tuple of words separated by newline characters
        """
        self.rows = puzzle.split()
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def search(self, word):
        """
        Searches for a word in the puzzle
        :param word: word to search for in puzzle
        :return: the points where the word can be found, None if the word does not exist in the puzzle
        :rtype: Point
        """
        # creates a generator object of points for each letter in the puzzle
        positions = (Point(x, y) for x in range(self.width) for y in range(self.height))
        for pos in positions:
            for plane_limit in PLANE_LIMITS:
                result = self.find_word(
                    word=word, position=pos, plane_limit=plane_limit
                )
                if result:
                    return result
        return None

    def find_word(self, word, position, plane_limit):
        """
        Finds the word on the puzzle given the word itself, the position (Point(x, y)) and the plane limit
        :param word: the word we are currently searching for, e.g python
        :param position: the current point on cartesian plan for the puzzle e.g Point(0, 0)
        :param plane_limit: the current plan limit, e.g Point(1, 0)
        :return: The Point where the whole word can be found
        :rtype: Point
        """
        # create a copy of the passed in position
        curr_position = copy(position)
        for let in word:
            if self.find_char(coord_point=curr_position) != let:
                return
            curr_position += plane_limit
        return position, curr_position - plane_limit

    def find_char(self, coord_point):
        """
        finds a character on the given puzzle
        :param coord_point: The current copy of the current point position being sought through
        :return:
        """
        if coord_point.x < 0 or coord_point.x >= self.width:
            return
        if coord_point.y < 0 or coord_point.y >= self.height:
            return
        # return the particular letter in the puzzled
        return self.rows[coord_point.y][coord_point.x]


def find_strings(grid: List[List[str]], words: List[str]) -> List[str]:
    """
    Finds the strings in the grid
    Args:
        grid (List[List[str]]): The grid to search through
        words (List[str]): The words to search for
    Returns:
        List[str]: The words that were found in the grid
    """
    trie = Trie()
    for word in words:
        trie.insert(word)

    if not grid or not grid[0]:
        return []

    rows_count, cols_count = len(grid), len(grid[0])
    result = []

    visited: Set[Tuple[int, int]] = set()

    # directions to move in the grid horizontally and vertically from a given cell
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # lambda function to check if the current cell is within the grid
    is_cell_within_grid = lambda r, c: 0 <= r < rows_count and 0 <= c < cols_count

    def dfs(row: int, col: int, node: TrieNode, path: str):
        """
        Depth-first search to find the words in the grid
        Args:
            row (int): The row of the current cell
            col (int): The column of the current cell
            node (TrieNode): The current node in the trie
            path (str): The current path of the word
        """
        # check if the current node is a word
        if node.is_end:
            result.append(path)
            # prevent duplicates
            node.is_end = False
            # prune the word from the trie
            trie.remove_characters(path)

            # We don't want to exit early, we want to continue searching for other words this is because from this node
            # other words can potentially be found.

        # mark visited
        visited.add((row, col))

        # explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # three specific conditions must be met before calling dfs recursively
            # 1. the new cell must be within the grid
            # 2. the new cell must not be visited
            # 3. the new cell must be a child of the current node
            if (
                is_cell_within_grid(new_row, new_col)
                and (new_row, new_col) not in visited
                and grid[new_row][new_col] in node.children
            ):
                new_character = grid[new_row][new_col]
                dfs(
                    new_row, new_col, node.children[new_character], path + new_character
                )

        # backtracking, remove the visited cell
        # so that we can explore other paths
        # By removing it, we ensure the cell is available again when the algorithm explores a completely different path
        # from a different starting point
        visited.remove((row, col))

    for row in range(rows_count):
        for col in range(cols_count):
            char = grid[row][col]
            if char in trie.root.children:
                dfs(row, col, trie.root.children[char], char)

    return result
