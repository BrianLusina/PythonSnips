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
    result = []
    word_len = len(letters)
    used_letters = [False] * word_len
    start = 0
    path_taken = []

    def dfs(start_index: int, path: List[str], used: List[bool]) -> None:
        nonlocal result
        if start_index == word_len:
            result.append("".join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue

            # add the letter to permutation, mark the letter as used
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used)
            # remove the letter from permutation, mark the letter as unused
            path.pop()
            used[i] = False

    dfs(start, path_taken, used_letters)

    return result


def permute_word(word: str) -> List[str]:
    result = []
    word_len = len(word)

    def permute_str(letters: str, current_index):
        nonlocal result
        if current_index == word_len - 1:
            result.append(letters)
            return

        for idx in range(current_index, word_len):
            swapped_str = swap_char(letters, current_index, idx)
            permute_str(swapped_str, current_index + 1)

    def swap_char(letters: str, i: int, j: int) -> str:
        """
        Swaps ith and jth indexes of the given string
        Args:
            letters (str): letters to find permutations for
            i (int): index of the first letter
            j (int): index of the second letter
        Returns:
            str: string with the letters at the ith and jth position swapped
        """
        swap_index = list(letters)
        swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
        return "".join(swap_index)

    permute_str(word, 0)
    return result
