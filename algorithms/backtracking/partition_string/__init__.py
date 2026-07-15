from typing import List
from algorithms.two_pointers.palindrome import is_palindrome


def partition(s: str) -> List[List[str]]:
    result = []
    word_length = len(s)

    def dfs(start: int, current_path: List[str]) -> None:
        if start == word_length:
            result.append(current_path[:])
            return

        for end in range(start + 1, word_length + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end, current_path + [prefix])

    dfs(0, [])
    return result
