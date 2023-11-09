from typing import List


def generate_permutations(letters: str) -> List[str]:
    """Generates permutations of the given letters and returns a list of all permutations.

    Args:
        letters (str): letters to find permutations for

    Returns:
        List: all the permutations of given letters.

    Time Complexity
        We have n letters to choose in the first level, n - 1 choices in the second level and so on therefore the number
        of strings we generate is n * (n - 1) * (n - 2) * ... * 1, or O(n!). Since each string has length n, generating
        all the strings requires O(n * n!) time.

    Space Complexity
        The total space complexity is given by the amount of space required by the strings we're constructing. Like the
        time complexity, the space complexity is also O(n * n!).
    """
    def dfs(start_index: int, path: List[str], used: List[bool], res: List[str]) -> None:
        if start_index == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue

            # add the letter to permutation, mark the letter as used
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used, res)
            # remove the letter from permutation, mark the letter as unused
            path.pop()
            used[i] = False

    result = []
    used_letters = [False] * len(letters)
    start = 0
    path_taken = []

    dfs(start, path_taken, used_letters, result)

    return result
