from typing import List


def letter_combination(n: int) -> List[str]:
    result = []

    if n == 0:
        return result

    def dfs(start_index: int, path: List[str]):
        if start_index == n:
            result.append("".join(path))
            return

        for letter in ["a", "b"]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return result
